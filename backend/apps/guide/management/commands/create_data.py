from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.categories.models import Category
from apps.places.models import Place, Favorite

User = get_user_model()


class Command(BaseCommand):
    help = "Создает тестовых пользователей и начальные данные"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("🎉 Начало создания тестовых данных..."))

        # Этап 1: Создание категорий
        self.stdout.write(self.style.SUCCESS("\n📁 ЭТАП 1: Создание категорий..."))
        
        categories = [
            {"name": "Спорт", "slug": "sport", "icon": "⚽"},
            {"name": "Культура", "slug": "culture", "icon": "🎭"},
            {"name": "История", "slug": "history", "icon": "🏛️"},
            {"name": "Природа", "slug": "nature", "icon": "🌿"},
            {"name": "Путешествия", "slug": "travel", "icon": "🏞️"},
            {"name": "Развлечения", "slug": "entertainments", "icon": "🍿"},
            {"name": "Еда", "slug": "meal", "icon": "🍴"},
        ]

        category_objects = {}
        for c in categories:
            category, created = Category.objects.get_or_create(
                slug=c["slug"], defaults=c
            )
            category_objects[c["slug"]] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Категория создана: {category.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Категория уже существует: {category.name}"))

        # Этап 2: Создание спортивных мест
        self.stdout.write(self.style.SUCCESS("\n🏃 ЭТАП 2: Создание спортивных мест (15 мест)..."))

        sport_places = [
            {
                "name": 'Горнолыжный курорт "Амирсой"',
                "slug": "amirsoy-ski-resort",
                "category": category_objects["sport"],
                "latitude": 41.4747, "longitude": 70.0882,
                "image": "places/sport/amirsoy.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Чимганские горы", 
                "slug": "chimgan-mountains",
                "category": category_objects["sport"], 
                "latitude": 41.5000, "longitude": 70.0833,
                "image": "places/sport/chimgan.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Чарвакское водохранилище", 
                "slug": "charvak-reservoir",
                "category": category_objects["sport"], 
                "latitude": 41.6333, "longitude": 70.0167,
                "image": "places/sport/charvak.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Humo Arena", 
                "slug": "humo-arena",
                "category": category_objects["sport"], 
                "latitude": 41.3500, "longitude": 69.2500,
                "image": "places/sport/humo.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Milliy Stadium", 
                "slug": "milliy-stadium",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/sport/milliy.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Спорткомплекс Юнусабад", 
                "slug": "yunusabad-sports-complex",
                "category": category_objects["sport"], 
                "latitude": 41.3667, "longitude": 69.2833,
                "image": "places/sport/yunusabad.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Теннисный корт Ташкент", 
                "slug": "tashkent-tennis-court",
                "category": category_objects["sport"], 
                "latitude": 41.3000, "longitude": 69.2667,
                "image": "places/sport/tennis.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Аквапарк Ташкент", 
                "slug": "tashkent-aquapark",
                "category": category_objects["sport"], 
                "latitude": 41.3333, "longitude": 69.2333,
                "image": "places/sport/aquapark.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Скалодром Алай", 
                "slug": "alay-climbing-wall",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/sport/climbing.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Велотрек Мирзо-Улугбек", 
                "slug": "mirzo-ulugbek-velodrome",
                "category": category_objects["sport"], 
                "latitude": 41.3500, "longitude": 69.2000,
                "image": "places/sport/velodrome.jpg", "rating": 4.2, "price_range": "$$",
            },
            {
                "name": "Гольф клуб Ташкент", 
                "slug": "tashkent-golf-club",
                "category": category_objects["sport"], 
                "latitude": 41.2667, "longitude": 69.1833,
                "image": "places/sport/golf.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Фитнес центр Premium", 
                "slug": "premium-fitness-center",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/sport/fitness.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Бассейн Олимпийский", 
                "slug": "olympic-swimming-pool",
                "category": category_objects["sport"], 
                "latitude": 41.2833, "longitude": 69.2333,
                "image": "places/sport/pool.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Стадион Пахтакор", 
                "slug": "pakhtakor-stadium",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2667,
                "image": "places/sport/pakhtakor.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Боулинг клуб Strike", 
                "slug": "strike-bowling-club",
                "category": category_objects["sport"], 
                "latitude": 41.3333, "longitude": 69.2167,
                "image": "places/sport/bowling.jpg", "rating": 4.2, "price_range": "$$",
            },
        ]

        self._create_places(sport_places, "спортивных")

        # Этап 3: Создание культурных мест
        self.stdout.write(self.style.SUCCESS("\n🎭 ЭТАП 3: Создание культурных мест (15 мест)..."))

        culture_places = [
            {
                "name": "Государственный музей истории Узбекистана",
                "slug": "state-museum-of-history",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/culture/history_museum.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Театр оперы и балета имени Алишера Навои",
                "slug": "navoi-theater", 
                "category": category_objects["culture"],
                "latitude": 41.3167, "longitude": 69.2833,
                "image": "places/culture/navoi_theater.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Музей искусств Узбекистана", 
                "slug": "art-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2667,
                "image": "places/culture/art_museum.jpg", "rating": 4.4, "price_range": "$",
            },
            {
                "name": "Медресе Кукельдаш", 
                "slug": "kukeldash-madrasah",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2333,
                "image": "places/culture/kukeldash.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Дворец международных форумов", 
                "slug": "international-forum-palace",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.3000,
                "image": "places/culture/forum_palace.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Театр Ильхом", 
                "slug": "ilhom-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/culture/ilhom.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Галерея изобразительных искусств", 
                "slug": "fine-arts-gallery",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2000,
                "image": "places/culture/gallery.jpg", "rating": 4.2, "price_range": "$",
            },
            {
                "name": "Концертный зал Дружбы народов", 
                "slug": "friendship-concert-hall",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1833,
                "image": "places/culture/concert_hall.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Кукольный театр", 
                "slug": "puppet-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1667,
                "image": "places/culture/puppet.jpg", "rating": 4.1, "price_range": "$",
            },
            {
                "name": "Музей прикладного искусства", 
                "slug": "applied-arts-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1500,
                "image": "places/culture/applied_arts.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Театр драмы имени Хамзы", 
                "slug": "hamza-drama-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1333,
                "image": "places/culture/drama.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Центр современного искусства", 
                "slug": "contemporary-art-center",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1167,
                "image": "places/culture/contemporary.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Музей литературы", 
                "slug": "literature-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1000,
                "image": "places/culture/literature.jpg", "rating": 4.0, "price_range": "$",
            },
            {
                "name": "Филармония Узбекистана", 
                "slug": "uzbekistan-philharmonic",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.0833,
                "image": "places/culture/philharmonic.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Кинотеатр 4D", 
                "slug": "4d-cinema",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.0667,
                "image": "places/culture/cinema.jpg", "rating": 4.2, "price_range": "$$",
            },
        ]

        self._create_places(culture_places, "культурных")

        # Этап 4: Создание исторических мест
        self.stdout.write(self.style.SUCCESS("\n🏛️ ЭТАП 4: Создание исторических мест (15 мест)..."))

        history_places = [
            {
                "name": "Площадь Хаст-Имам", 
                "slug": "hast-imam-square",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2400,
                "image": "places/history/hast_imam.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Мавзолей Каффаль Шаши", 
                "slug": "kaffal-shashi-mausoleum",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2450,
                "image": "places/history/kaffal.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Мечеть Минор", 
                "slug": "minor-mosque",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2500,
                "image": "places/history/minor.jpg", "rating": 4.7, "price_range": "$",
            },
            {
                "name": "Комплекс Хазрати Имам", 
                "slug": "hazrati-imam-complex",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2550,
                "image": "places/history/hazrati.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Медресе Барак-Хан", 
                "slug": "barak-khan-madrasah",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2600,
                "image": "places/history/barak.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Мавзолей Зангиата", 
                "slug": "zangiata-mausoleum",
                "category": category_objects["history"], 
                "latitude": 41.1967, "longitude": 69.1450,
                "image": "places/history/zangiata.jpg", "rating": 4.4, "price_range": "$",
            },
            {
                "name": "Городище Афрасиаб", 
                "slug": "afrasiab-settlement",
                "category": category_objects["history"], 
                "latitude": 39.6667, "longitude": 66.9833,
                "image": "places/history/afrasiab.jpg", "rating": 4.7, "price_range": "$",
            },
            {
                "name": "Обсерватория Улугбека", 
                "slug": "ulugbek-observatory",
                "category": category_objects["history"], 
                "latitude": 39.6667, "longitude": 66.9667,
                "image": "places/history/ulugbek.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Мавзолей Гур-Эмир", 
                "slug": "gur-emir-mausoleum",
                "category": category_objects["history"], 
                "latitude": 39.6500, "longitude": 66.9667,
                "image": "places/history/gur_emir.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Мечеть Биби-Ханым", 
                "slug": "bibi-khanym-mosque",
                "category": category_objects["history"], 
                "latitude": 39.6600, "longitude": 66.9750,
                "image": "places/history/bibi.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Шахи-Зинда", 
                "slug": "shahi-zinda",
                "category": category_objects["history"], 
                "latitude": 39.6633, "longitude": 66.9833,
                "image": "places/history/shahi.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Регистан Самарканда", 
                "slug": "registan-samarkand",
                "category": category_objects["history"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/history/registan.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Крепость Арк", 
                "slug": "ark-fortress",
                "category": category_objects["history"], 
                "latitude": 39.7767, "longitude": 64.4133,
                "image": "places/history/ark.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Мавзолей Чашма-Аюб", 
                "slug": "chashma-ayub-mausoleum",
                "category": category_objects["history"], 
                "latitude": 39.7733, "longitude": 64.4167,
                "image": "places/history/chashma.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Мечеть Боло-Хауз", 
                "slug": "bolo-khauz-mosque",
                "category": category_objects["history"], 
                "latitude": 39.7750, "longitude": 64.4150,
                "image": "places/history/bolo.jpg", "rating": 4.4, "price_range": "$",
            },
        ]

        self._create_places(history_places, "исторических")

        # Этап 5: Создание природных мест
        self.stdout.write(self.style.SUCCESS("\n🌿 ЭТАП 5: Создание природных мест (15 мест)..."))

        nature_places = [
            {
                "name": "Ботанический сад", 
                "slug": "botanical-garden",
                "category": category_objects["nature"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/nature/botanical.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Янгиобод", 
                "slug": "yangiobod",
                "category": category_objects["nature"], 
                "latitude": 41.1167, "longitude": 69.9167,
                "image": "places/nature/yangiobod.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Угам-Чаткальский национальный парк", 
                "slug": "ugam-chatkal-national-park",
                "category": category_objects["nature"], 
                "latitude": 41.5000, "longitude": 70.0833,
                "image": "places/nature/ugam.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Горы Нуратау", 
                "slug": "nuratau-mountains",
                "category": category_objects["nature"], 
                "latitude": 40.5000, "longitude": 66.6667,
                "image": "places/nature/nuratau.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Озеро Айдаркуль", 
                "slug": "aydarkul-lake",
                "category": category_objects["nature"], 
                "latitude": 40.9167, "longitude": 66.8333,
                "image": "places/nature/aydarkul.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Плато Пулатхан", 
                "slug": "pulathan-plateau",
                "category": category_objects["nature"], 
                "latitude": 41.0833, "longitude": 70.1667,
                "image": "places/nature/pulathan.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Водопад Арсланбоб", 
                "slug": "arslanbob-waterfall",
                "category": category_objects["nature"], 
                "latitude": 41.3333, "longitude": 72.4333,
                "image": "places/nature/arslanbob.jpg", "rating": 4.9, "price_range": "$$",
            },
            {
                "name": "Сайрокские озера", 
                "slug": "sayrok-lakes",
                "category": category_objects["nature"], 
                "latitude": 41.2500, "longitude": 70.1667,
                "image": "places/nature/sayrok.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Каньон Сангардак", 
                "slug": "sangardak-canyon",
                "category": category_objects["nature"], 
                "latitude": 38.2500, "longitude": 67.9000,
                "image": "places/nature/sangardak.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Заповедник Кызылкум", 
                "slug": "kyzylkum-reserve",
                "category": category_objects["nature"], 
                "latitude": 42.0000, "longitude": 63.0000,
                "image": "places/nature/kyzylkum.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Гора Большой Чимган", 
                "slug": "big-chimgan-mountain",
                "category": category_objects["nature"], 
                "latitude": 41.4833, "longitude": 70.0333,
                "image": "places/nature/big_chimgan.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Урочище Аманкутан", 
                "slug": "amankutan-gorge",
                "category": category_objects["nature"], 
                "latitude": 39.4167, "longitude": 67.0333,
                "image": "places/nature/amankutan.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Озеро Тудакуль", 
                "slug": "tudakul-lake",
                "category": category_objects["nature"], 
                "latitude": 40.0833, "longitude": 64.6333,
                "image": "places/nature/tudakul.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Нуратинский заповедник", 
                "slug": "nurata-reserve",
                "category": category_objects["nature"], 
                "latitude": 40.5000, "longitude": 66.6667,
                "image": "places/nature/nurata.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Гиссарский хребет", 
                "slug": "hissar-range",
                "category": category_objects["nature"], 
                "latitude": 38.5000, "longitude": 68.0000,
                "image": "places/nature/hissar.jpg", "rating": 4.6, "price_range": "$$",
            },
        ]

        self._create_places(nature_places, "природных")

        # Этап 6: Создание мест для путешествий
        self.stdout.write(self.style.SUCCESS("\n🏞️ ЭТАП 6: Создание мест для путешествий (15 мест)..."))

        travel_places = [
            {
                "name": "Дорога в Чимган", 
                "slug": "road-to-chimgan",
                "category": category_objects["travel"], 
                "latitude": 41.4000, "longitude": 69.9167,
                "image": "places/travel/chimgan_road.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Тур по древним городам", 
                "slug": "ancient-cities-tour",
                "category": category_objects["travel"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/travel/ancient_tour.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Экскурсия по Ташкенту", 
                "slug": "tashkent-excursion",
                "category": category_objects["travel"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/travel/tashkent_tour.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Путешествие в Нурату", 
                "slug": "nurata-journey",
                "category": category_objects["travel"], 
                "latitude": 40.5000, "longitude": 65.6667,
                "image": "places/travel/nurata_tour.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Тур по Ферганской долине", 
                "slug": "fergana-valley-tour",
                "category": category_objects["travel"], 
                "latitude": 40.3864, "longitude": 71.7864,
                "image": "places/travel/fergana.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Экспедиция в Кызылкум", 
                "slug": "kyzylkum-expedition",
                "category": category_objects["travel"], 
                "latitude": 42.0000, "longitude": 63.5000,
                "image": "places/travel/kyzylkum_exp.jpg", "rating": 4.4, "price_range": "$$$",
            },
            {
                "name": "Тур по Великому шелковому пути", 
                "slug": "silk-road-tour",
                "category": category_objects["travel"], 
                "latitude": 40.1000, "longitude": 67.8333,
                "image": "places/travel/silk_road.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Путешествие на Аральское море", 
                "slug": "aral-sea-journey",
                "category": category_objects["travel"], 
                "latitude": 45.0000, "longitude": 59.0000,
                "image": "places/travel/aral.jpg", "rating": 4.3, "price_range": "$$$",
            },
            {
                "name": "Тур по Хорезму", 
                "slug": "khorezm-tour",
                "category": category_objects["travel"], 
                "latitude": 41.5500, "longitude": 60.6333,
                "image": "places/travel/khorezm.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Экскурсия в Шахрисабз", 
                "slug": "shahrisabz-excursion",
                "category": category_objects["travel"], 
                "latitude": 39.0578, "longitude": 66.8342,
                "image": "places/travel/shahrisabz.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Тур по Бухаре", 
                "slug": "bukhara-tour",
                "category": category_objects["travel"], 
                "latitude": 39.7667, "longitude": 64.4167,
                "image": "places/travel/bukhara.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Путешествие в Термез", 
                "slug": "termez-journey",
                "category": category_objects["travel"], 
                "latitude": 37.2242, "longitude": 67.2783,
                "image": "places/travel/termez.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Экотуризм в Заамин", 
                "slug": "zaamin-ecotourism",
                "category": category_objects["travel"], 
                "latitude": 39.9667, "longitude": 68.4000,
                "image": "places/travel/zaamin.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Тур по Самарканду", 
                "slug": "samarkand-tour",
                "category": category_objects["travel"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/travel/samarkand_tour.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Путешествие в Карши", 
                "slug": "karshi-journey",
                "category": category_objects["travel"], 
                "latitude": 38.8667, "longitude": 65.8000,
                "image": "places/travel/karshi.jpg", "rating": 4.4, "price_range": "$$",
            },
        ]

        self._create_places(travel_places, "путешествий")

        # Этап 7: Создание развлекательных мест
        self.stdout.write(self.style.SUCCESS("\n🍿 ЭТАП 7: Создание развлекательных мест (15 мест)..."))

        entertainment_places = [
            {
                "name": "Парк Ашхабад", 
                "slug": "ashgabat-park",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2833,
                "image": "places/entertainment/ashgabat.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Развлекательный центр Next", 
                "slug": "next-entertainment-center",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/entertainment/next.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Кинотеатр Star", 
                "slug": "star-cinema",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2333,
                "image": "places/entertainment/star.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Луна-парк", 
                "slug": "luna-park",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/entertainment/luna.jpg", "rating": 4.2, "price_range": "$$",
            },
            {
                "name": "Боулинг клуб Victory", 
                "slug": "victory-bowling",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2000,
                "image": "places/entertainment/victory.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Караоке клуб Melody", 
                "slug": "melody-karaoke",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1833,
                "image": "places/entertainment/melody.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Бильярдный клуб Champion", 
                "slug": "champion-billiards",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1667,
                "image": "places/entertainment/champion.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Игровая зона GameZone", 
                "slug": "gamezone-arcade",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1500,
                "image": "places/entertainment/gamezone.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "ТРЦ Samarkand Darvoza", 
                "slug": "samarkand-darvoza-mall",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1333,
                "image": "places/entertainment/darvoza.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Комплекс Magic City", 
                "slug": "magic-city-complex",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1167,
                "image": "places/entertainment/magic.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Квест комната Escape", 
                "slug": "escape-quest-room",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1000,
                "image": "places/entertainment/escape.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Виртуальная реальность VR Zone", 
                "slug": "vr-zone",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.0833,
                "image": "places/entertainment/vr.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Картинг центр Speed", 
                "slug": "speed-karting",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.0667,
                "image": "places/entertainment/speed.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Тир Sharpshooter", 
                "slug": "sharpshooter-range",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.0500,
                "image": "places/entertainment/sharpshooter.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Детский развлекательный центр", 
                "slug": "kids-entertainment-center",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.0333,
                "image": "places/entertainment/kids.jpg", "rating": 4.3, "price_range": "$$",
            },
        ]

        self._create_places(entertainment_places, "развлекательных")

        # Этап 8: Создание мест для еды
        self.stdout.write(self.style.SUCCESS("\n🍴 ЭТАП 8: Создание мест для еды (15 мест)..."))

        meal_places = [
            {
                "name": "Ресторан узбекской кухни", 
                "slug": "uzbek-cuisine-restaurant",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/meal/uzbek.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Кафе European", 
                "slug": "european-cafe",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.2667,
                "image": "places/meal/european.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Чайхана Navruz", 
                "slug": "navruz-teahouse",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.2833,
                "image": "places/meal/navruz.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Ресторан Afsona", 
                "slug": "afsona-restaurant",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3000,
                "image": "places/meal/afsona.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Кафе Caravan", 
                "slug": "caravan-cafe",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3167,
                "image": "places/meal/caravan.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Ресторан Silk Road", 
                "slug": "silk-road-restaurant",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3333,
                "image": "places/meal/silk_road_rest.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Бистро Paris", 
                "slug": "paris-bistro",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3500,
                "image": "places/meal/paris.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Кофейня Coffee Lab", 
                "slug": "coffee-lab",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3667,
                "image": "places/meal/coffee_lab.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Ресторан мексиканской кухни", 
                "slug": "mexican-restaurant",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.3833,
                "image": "places/meal/mexican.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Суши-бар Tokyo", 
                "slug": "tokyo-sushi-bar",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.4000,
                "image": "places/meal/tokyo.jpg", "rating": 4.6, "price_range": "$$$",
            },
            {
                "name": "Пиццерия Италия", 
                "slug": "italia-pizzeria",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.4167,
                "image": "places/meal/italia.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Бургерная American", 
                "slug": "american-burger",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.4333,
                "image": "places/meal/american.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Вегетарианское кафе Green", 
                "slug": "green-vegetarian",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.4500,
                "image": "places/meal/green.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Кондитерская Sweet", 
                "slug": "sweet-confectionery",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.4667,
                "image": "places/meal/sweet.jpg", "rating": 4.9, "price_range": "$$",
            },
            {
                "name": "Уличная еда Чорсу", 
                "slug": "chorzu-street-food",
                "category": category_objects["meal"], 
                "latitude": 41.3167, "longitude": 69.2333,
                "image": "places/meal/chorzu.jpg", "rating": 4.6, "price_range": "$",
            },
        ]

        self._create_places(meal_places, "ресторанов")

        self.stdout.write(
            self.style.SUCCESS(f"\n🎉 Все тестовые данные успешно созданы! Всего мест: {Place.objects.count()}")
        )

    def _create_places(self, places_list, category_name):
        """Вспомогательная функция для создания мест"""
        created_count = 0
        for p in places_list:
            place, created = Place.objects.get_or_create(
                slug=p["slug"],
                defaults={
                    "name": p["name"],
                    "category": p["category"],
                    "latitude": p["latitude"],
                    "longitude": p["longitude"],
                    "image": p["image"],
                    "rating": p["rating"],
                    "price_range": p["price_range"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"   ✅ Создано: {place.name}"))

        self.stdout.write(self.style.SUCCESS(f"   📊 Создано {created_count} {category_name} мест"))
