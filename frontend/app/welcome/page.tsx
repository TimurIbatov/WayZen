"use client";

import { Button } from "@/components/ui/button";
import { Compass, MapPin, Users, Zap, Globe } from "lucide-react";
import { useRouter } from "next/navigation";
import { useLanguage } from "@/lib/hooks/use-language";
// Убрали LanguageSelector, так как создаём свою кнопку

export default function WelcomePage() {
  const router = useRouter();
  const { t, changeLanguage } = useLanguage(); // Добавили changeLanguage для переключения

  // Пример переключения языка (замени на свою логику)
  const toggleLanguage = () => {
    changeLanguage(t.locale === "en" ? "ru" : "en");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/20 to-teal-900/20 flex flex-col relative overflow-hidden">
      {/* Decorative gradient semicircle at top */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-64 rounded-b-full bg-gradient-to-b from-gray-700/40 to-transparent blur-3xl pointer-events-none" />

      {/* Header with custom language button in top right corner */}
      <div className="relative z-20 p-6 md:p-8">
        <div className="absolute top-4 right-4">
          <button
            onClick={toggleLanguage}
            className="p-5 bg-white-500 text-white rounded-full shadow-xl hover:bg-red-600 transition-all flex items-center gap-2 min-w-[50px]"
          >
            <Globe className="h-5 w-5" />
          </button>
        </div>
      </div>

      {/* Main content */}
      <div className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10">
        <div className="max-w-6xl w-full">
          {/* Hero section */}
          <div className="text-center space-y-8 mb-16">
            <div className="space-y-4">
              <h1 className="text-7xl font-bold text-white italic">WayZen</h1>
              <p className="text-lg md:text-xl text-teal-400 font-medium">{t("welcome.tagline")}</p>
              <h2 className="text-5xl md:text-7xl font-bold text-white leading-tight text-balance">
                {t("welcome.title")}
              </h2>
              <p className="text-lg md:text-xl text-gray-300 leading-relaxed text-balance max-w-3xl mx-auto">
                {t("welcome.description")}
              </p>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center pt-4">
              <Button
                onClick={() => router.push("/login")}
                size="lg"
                className="bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white px-12 py-6 text-lg font-semibold rounded-full shadow-lg hover:shadow-xl transition-all"
              >
                <Compass className="h-5 w-5 mr-2" />
                {t("welcome.startJourney")}
              </Button>
              <Button
                onClick={() => router.push("/login")}
                size="lg"
                variant="outline"
                className="border-2 border-teal-400 text-teal-400 hover:bg-teal-400/10 px-12 py-6 text-lg font-semibold rounded-full transition-all"
              >
                {t("welcome.login")}
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <div className="text-center py-6 text-gray-500 text-sm border-t border-slate-700/50 relative z-10">
        <p>© 2025 WayZen. Откройте скрытые жемчужины Узбекистана</p>
      </div>
    </div>
  );
}