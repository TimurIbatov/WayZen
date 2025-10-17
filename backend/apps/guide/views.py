from django.http import StreamingHttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone
from django.shortcuts import get_object_or_404
import google.generativeai as genai
import json
import logging
from .models import ChatSession, Message

# --- Настройка логирования ---
logger = logging.getLogger(__name__)

# --- Инициализация Gemini ---
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    logger.info("Gemini AI успешно инициализирован")
except Exception as e:
    logger.error(f"Ошибка инициализации Gemini: {e}")
    model = None

# --- Системные настройки ---
SYSTEM_PROMPT_SETUP = (
    "Ты выступаешь как Wayzen AI — элегантный, дружелюбный гид для туристов. "
    "Отвечай только на темы, связанные с путешествиями, культурой и достопримечательностями. "
    "Если вопрос не по теме, откажись вежливо и с чувством стиля."
)

FIRST_GREETING = (
    "Приветствую! Я **Wayzen AI**, ваш личный гид в мире путешествий. "
    "С радостью расскажу о культуре, традициях и чудесных местах планеты."
)

# --- Вспомогательные функции ---
def _generate_chat_title(user_prompt: str) -> str:
    """Генерирует заголовок чата на основе первого сообщения пользователя"""
    if len(user_prompt) > 30:
        return user_prompt[:30] + "..."
    return user_prompt or "Новый чат"

def _prepare_chat_history(chat_history: list, is_first_message: bool = False) -> list:
    """Подготавливает историю чата для Gemini API"""
    full_history = [
        {"role": "user", "parts": [{"text": SYSTEM_PROMPT_SETUP}]},
        {"role": "model", "parts": [{"text": "Понял. Приступаю к роли."}]}
    ]
    
    if chat_history:
        full_history.extend(chat_history)
    
    return full_history

# --- Основной эндпоинт для общения ---
@csrf_exempt
@require_POST
def ask(request):
    if not model:
        logger.error("Попытка использования неинициализированной модели Gemini")
        return JsonResponse({"error": "Gemini API не настроен."}, status=500)

    try:
        data = json.loads(request.body.decode("utf-8"))
        user_prompt = data.get("prompt", "").strip()
        chat_id = data.get("chat_id")
        chat_history = data.get("history", [])
        
        if not user_prompt:
            return JsonResponse({"error": "Пустой запрос"}, status=400)
            
    except json.JSONDecodeError:
        logger.warning("Невалидный JSON в запросе")
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        logger.error(f"Ошибка обработки запроса: {e}")
        return JsonResponse({"error": "Ошибка обработки запроса"}, status=400)

    # Создание или получение чата
    try:
        if chat_id:
            chat = get_object_or_404(ChatSession, id=chat_id)
            # Обновляем время последней активности
            chat.updated_at = timezone.now()
            chat.save()
        else:
            chat_title = _generate_chat_title(user_prompt)
            chat = ChatSession.objects.create(
                user=request.user if request.user.is_authenticated else None,
                title=chat_title
            )
            logger.info(f"Создан новый чат: {chat.id}")

        # Сохраняем сообщение пользователя
        user_message = Message.objects.create(
            chat=chat, 
            role="user", 
            content=user_prompt
        )

    except Exception as e:
        logger.error(f"Ошибка работы с базой данных: {e}")
        return JsonResponse({"error": "Ошибка базы данных"}, status=500)

    is_first_message = len(chat_history) == 0
    full_history = _prepare_chat_history(chat_history, is_first_message)

    def generate():
        response_text = ""
        try:
            chat_session = model.start_chat(history=full_history)
            
            # Отправляем приветствие для первого сообщения
            if is_first_message:
                yield f"data: {json.dumps({'type': 'greeting', 'content': FIRST_GREETING})}\n\n"

            # Отправляем основной ответ
            response_stream = chat_session.send_message(user_prompt, stream=True)
            
            for chunk in response_stream:
                if chunk.text:
                    response_text += chunk.text
                    yield f"data: {json.dumps({'type': 'chunk', 'content': chunk.text})}\n\n"

            # Сохраняем ответ модели
            if response_text:
                Message.objects.create(
                    chat=chat, 
                    role="model", 
                    content=response_text
                )
                logger.info(f"Сообщение сохранено в чат {chat.id}")

            # Сигнал завершения
            yield f"data: {json.dumps({'type': 'complete'})}\n\n"

        except Exception as e:
            error_msg = f"Ошибка генерации ответа: {str(e)}"
            logger.error(error_msg)
            yield f"data: {json.dumps({'type': 'error', 'content': error_msg})}\n\n"

    return StreamingHttpResponse(
        generate(), 
        content_type="text/event-stream",
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'  # Для nginx
        }
    )

# --- История чата ---
@require_GET
def get_chat_history(request, chat_id):
    try:
        chat = get_object_or_404(ChatSession, id=chat_id)
        chat_messages = chat.messages.order_by("created_at")
        
        history = [
            {
                "id": msg.id,
                "role": msg.role, 
                "content": msg.content,
                "created_at": msg.created_at.isoformat()
            }
            for msg in chat_messages
        ]
        
        return JsonResponse({
            "chat_id": chat.id,
            "title": chat.title,
            "created_at": chat.created_at.isoformat(),
            "history": history
        })
        
    except Exception as e:
        logger.error(f"Ошибка получения истории чата {chat_id}: {e}")
        return JsonResponse({"error": "Ошибка сервера"}, status=500)

# --- Список чатов ---
@require_GET
def get_user_chats(request):
    try:
        # Для анонимных пользователей возвращаем все чаты
        # В реальном приложении нужно добавить фильтрацию по пользователю
        chats = ChatSession.objects.all().order_by("-updated_at")
        
        result = [
            {
                "id": chat.id,
                "title": chat.title,
                "created_at": chat.created_at.isoformat(),
                "updated_at": chat.updated_at.isoformat(),
                "message_count": chat.messages.count()
            }
            for chat in chats
        ]
        
        return JsonResponse({"chats": result}, safe=False)
        
    except Exception as e:
        logger.error(f"Ошибка получения списка чатов: {e}")
        return JsonResponse({"error": "Ошибка сервера"}, status=500)

# --- Удаление чата ---
@csrf_exempt
@require_POST
def delete_chat(request, chat_id):
    try:
        chat = get_object_or_404(ChatSession, id=chat_id)
        chat_title = chat.title
        chat.delete()
        
        logger.info(f"Чат {chat_id} удален")
        return JsonResponse({
            "success": True, 
            "message": f"Чат '{chat_title}' удален"
        })
        
    except Exception as e:
        logger.error(f"Ошибка удаления чата {chat_id}: {e}")
        return JsonResponse({"error": "Ошибка удаления чата"}, status=500)

# --- Статус API ---
@require_GET
def health_check(request):
    """Проверка статуса API и подключения к Gemini"""
    status = {
        "api_status": "healthy",
        "gemini_configured": model is not None,
        "timestamp": timezone.now().isoformat()
    }
    
    if model is None:
        status["api_status"] = "degraded"
        status["error"] = "Gemini не настроен"
    
    return JsonResponse(status)
