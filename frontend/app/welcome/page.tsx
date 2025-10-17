"use client"

import { Button } from "@/components/ui/button"
import { Compass } from "lucide-react"
import { useRouter } from "next/navigation"

export default function WelcomePage() {
  const router = useRouter()

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/20 to-teal-900/20 flex items-center justify-center p-8">
      <div className="max-w-4xl text-center space-y-12">
        <div className="flex items-center justify-center gap-3">
          <h1 className="text-7xl font-bold text-white italic">WayZen</h1>
        </div>

        {/* Tagline */}
        <div className="space-y-4">
          <p className="text-xl text-teal-400 font-medium">Ваш AI помощник для путешествий ✈️</p>
          <h2 className="text-5xl md:text-6xl font-bold text-white leading-tight text-balance">
            Откройте для себя
            <br />
            Узбекистан
          </h2>
          <p className="text-xl text-gray-300 leading-relaxed text-balance max-w-2xl mx-auto">
            Персонализированные рекомендации, умный маршрутизатор и местные секреты - все в одном месте
          </p>
          
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <Button
            onClick={() => router.push("/login")}
            size="lg"
            className="bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white px-12 py-6 text-lg font-semibold rounded-full shadow-lg hover:shadow-xl transition-all"
          >
            <Compass className="h-5 w-5 mr-2" />
            Начать путешествие
          </Button>
          <Button
            onClick={() => router.push("/login")}
            size="lg"
            variant="outline"
            className="border-2 border-teal-400 text-teal-400 hover:bg-teal-400/10 px-12 py-6 text-lg font-semibold rounded-full transition-all"
          >
            Войти
          </Button>
        </div>
      </div>
    </div>
  )
}
