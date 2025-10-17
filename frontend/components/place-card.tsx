"use client"

import { Star, MapPin, Heart } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import type { Place } from "@/lib/types"
import Link from "next/link"
import Image from "next/image"

interface PlaceCardProps {
  place: Place
  isFavorite: boolean
  onToggleFavorite: (placeId: string) => void
}

export function PlaceCard({ place, isFavorite, onToggleFavorite }: PlaceCardProps) {
  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow border-border">
      <Link href={`/place/${place.id}`}>
        <div className="relative h-48 bg-muted">
          <Image src={place.images[0] || "/placeholder.svg"} alt={place.name} fill className="object-cover" />
          {place.isHidden && <Badge className="absolute top-2 left-2 bg-gold text-brown">Скрытая жемчужина</Badge>}
        </div>
      </Link>
      <CardContent className="p-4">
        <div className="flex items-start justify-between gap-2 mb-2">
          <Link href={`/place/${place.id}`} className="flex-1">
            <h3 className="font-semibold text-foreground hover:text-primary transition-colors line-clamp-1">
              {place.name}
            </h3>
          </Link>
          <Button
            variant="ghost"
            size="icon"
            onClick={(e) => {
              e.preventDefault()
              onToggleFavorite(place.id)
            }}
            className="flex-shrink-0"
          >
            <Heart className={`h-5 w-5 ${isFavorite ? "fill-gold text-gold" : "text-muted-foreground"}`} />
          </Button>
        </div>

        <div className="flex items-center gap-1 text-sm text-muted-foreground mb-2">
          <MapPin className="h-4 w-4" />
          <span className="line-clamp-1">{place.city}</span>
        </div>

        <div className="flex items-center gap-1 mb-3">
          <Star className="h-4 w-4 fill-gold text-gold" />
          <span className="font-medium text-foreground">{place.rating}</span>
          <span className="text-sm text-muted-foreground">({place.reviewCount})</span>
        </div>

        <p className="text-sm text-muted-foreground line-clamp-2 leading-relaxed">{place.description}</p>

        <div className="flex flex-wrap gap-2 mt-3">
          {place.tags.slice(0, 3).map((tag) => (
            <Badge key={tag} variant="secondary" className="text-xs">
              {tag}
            </Badge>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
