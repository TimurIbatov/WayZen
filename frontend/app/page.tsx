"use client"

import type React from "react"
import { useState, useEffect, useRef } from "react"
import { Send, Map } from "lucide-react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/lib/hooks/use-auth"
import { storage } from "@/lib/storage"
import type { Place, Tour } from "@/lib/types"
import { PlaceCard } from "@/components/place-card"
import { VerticalNav } from "@/components/vertical-nav"
import { calculateTripCost, generateRoute } from "@/lib/cost-calculator"
import { useFavorites } from "@/lib/hooks/use-favorites"
import { useLanguage } from "@/lib/hooks/use-language"
import { Button } from "@/components/ui/button"
import { RouteModal } from "@/components/route-modal"
import { MobileNav } from "@/components/mobile-nav"
import { TourCard } from "@/components/tour-card"

export default function HomePage() {
  const router = useRouter()
  const { user } = useAuth()
  const { favorites, toggleFavorite } = useFavorites()
  const { t } = useLanguage()
  const [input, setInput] = useState("")
  const [recommendedPlaces, setRecommendedPlaces] = useState<Place[]>([])
  const [recommendedTours, setRecommendedTours] = useState<Tour[]>([])
  const [tripInfo, setTripInfo] = useState<{ cost: number; route: string[] } | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [isRouteModalOpen, setIsRouteModalOpen] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (!user) {
      router.push("/welcome")
    }
  }, [user, router])

  useEffect(() => {
    if (user) {
      const places = storage.getPlaces()
      const tours = storage.getTours()
      const userCity = localStorage.getItem("userCity")

      let filteredPlaces: Place[] = []
      let filteredTours: Tour[] = []

      if (user.interests && user.interests.length > 0) {
        filteredPlaces = places.filter((place) => user.interests.includes(place.categoryId))
        filteredTours = tours.filter(
          (tour) =>
            tour.isActive &&
            tour.places.some((placeId) => {
              const place = places.find((p) => p.id === placeId)
              return place && user.interests.includes(place.categoryId)
            }),
        )
      } else {
        filteredPlaces = places
        filteredTours = tours.filter((tour) => tour.isActive)
      }

      if (userCity) {
        filteredPlaces = filteredPlaces.filter((place) => place.city.toLowerCase() === userCity.toLowerCase())
        filteredTours = filteredTours.filter((tour) => tour.city.toLowerCase() === userCity.toLowerCase())
      }

      const placesWithFallback = filteredPlaces.map((place) => ({
        ...place,
        image: place.images?.[0] || "/images/placeholder.jpg",
      }))

      // Разделяем на места и туры
      const shuffledPlaces = placesWithFallback.sort(() => Math.random() - 0.5).slice(0, 3)
      const shuffledTours = filteredTours.sort(() => Math.random() - 0.5).slice(0, 3)
      
      setRecommendedPlaces(shuffledPlaces)
      setRecommendedTours(shuffledTours)

      if (shuffledPlaces.length > 0) {
        const cost = calculateTripCost(shuffledPlaces, 1)
        const route = generateRoute(shuffledPlaces)
        setTripInfo({
          cost: Math.round(cost.totalCost),
          route: route.route,
        })
      }

      setIsLoading(false)
    }
  }, [user])

  const handleSubmit = () => {
    if (input.trim()) {
      router.push(`/chat?q=${encodeURIComponent(input)}`)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      handleSubmit()
    }
  }

  if (!user) return null

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/20 to-teal-900/20">
      <VerticalNav />
      <MobileNav />

      <div className="fixed top-0 left-1/2 -translate-x-1/2 w-full h-96 pointer-events-none">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-96 h-96 rounded-b-full bg-gradient-to-b from-slate-700/30 to-transparent blur-3xl"></div>
      </div>

      <div className="pl-0 lg:pl-20 p-4 md:p-8 pb-24 md:pb-8 relative z-10">
        <div className="max-w-7xl mx-auto space-y-12">
          {/* Search Section - Centered */}
          <div className="max-w-3xl mx-auto pt-20">
            <div className="relative">
              <input
                ref={inputRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder={t("chat.placeholder")}
                className="w-full bg-transparent text-white/90 placeholder:text-white/40 text-3xl px-4 py-6 pr-20 border-0 border-white/30 outline-none caret-white focus:border-white/50 transition-colors text-center"
              />
              <button
                onClick={handleSubmit}
                className="absolute right-4 top-1/2 -translate-y-1/2 bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-600 hover:to-cyan-600 rounded-full h-14 w-14 flex items-center justify-center transition-all"
              >
                <Send className="h-6 w-6 text-white" />
              </button>
            </div>
          </div>

          {/* Recommendations Section */}
          {!isLoading && (recommendedPlaces.length > 0 || recommendedTours.length > 0) && (
            <div className="space-y-12">
              {/* Top Places Section */}
              {recommendedPlaces.length > 0 && (
                <div className="space-y-6">
                  <div className="text-center">
                    <h2 className="text-3xl font-bold text-white mb-2">{t("home.topPlaces")}</h2>
                    <p className="text-gray-400">{t("home.recommendations")}</p>
                  </div>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {recommendedPlaces.map((place) => (
                      <PlaceCard
                        key={place.id}
                        place={place}
                        isFavorite={favorites.includes(place.id)}
                        onToggleFavorite={toggleFavorite}
                      />
                    ))}
                  </div>
                </div>
              )}

              {/* Top Tours Section */}
              {recommendedTours.length > 0 && (
                <div className="space-y-6">
                  <div className="text-center">
                    <h2 className="text-3xl font-bold text-white mb-2">{t("home.topTours")}</h2>
                    <p className="text-gray-400">{t("tours.subtitle")}</p>
                  </div>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {recommendedTours.map((tour) => (
                      <TourCard key={tour.id} tour={tour} />
                    ))}
                  </div>
                </div>
              )}

              {/* View All Buttons - Centered */}
              <div className="flex flex-col md:flex-row justify-center gap-4 pt-4">
                <Button
                  onClick={() => router.push("/map")}
                  className="bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-600 hover:to-cyan-600 px-8 py-6 text-lg"
                >
                  {t("home.viewAllLocations")}
                </Button>
                {tripInfo && (
                  <Button
                    onClick={() => setIsRouteModalOpen(true)}
                    className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 px-8 py-6 text-lg flex items-center gap-2"
                  >
                    <Map className="h-5 w-5" />
                    {t("map.routeView")}
                  </Button>
                )}
              </div>
            </div>
          )}

          {/* Loading State */}
          {isLoading && (
            <div className="text-center py-20">
              <div className="inline-block">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-teal-400"></div>
              </div>
              <p className="text-gray-400 text-lg mt-4">{t("home.loading")}</p>
            </div>
          )}

          {/* Empty State */}
          {!isLoading && recommendedPlaces.length === 0 && recommendedTours.length === 0 && (
            <div className="text-center py-20">
              <p className="text-gray-400 text-lg mb-4">{t("home.noRecommendations")}</p>
              <Button
                onClick={() => router.push("/map")}
                className="bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-600 hover:to-cyan-600"
              >
                {t("home.viewAllLocations")}
              </Button>
            </div>
          )}
        </div>
      </div>

      {tripInfo && (
        <RouteModal
          isOpen={isRouteModalOpen}
          onClose={() => setIsRouteModalOpen(false)}
          places={recommendedPlaces}
          route={tripInfo.route}
          cost={tripInfo.cost}
        />
      )}
    </div>
  )
}