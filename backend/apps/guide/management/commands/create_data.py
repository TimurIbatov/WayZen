from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.categories.models import Category
from apps.places.models import Place, Favorite

User = get_user_model()


class Command(BaseCommand):
    help = "Create test users and initial data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("🎉 Starting test data creation..."))

        # Step 1: Create categories
        self.stdout.write(self.style.SUCCESS("\n📁 STEP 1: Creating categories..."))
        
        categories = [
            {"name": "Sports", "slug": "sport", "icon": "⚽"},
            {"name": "Culture", "slug": "culture", "icon": "🎭"},
            {"name": "History", "slug": "history", "icon": "🏛️"},
            {"name": "Nature", "slug": "nature", "icon": "🌿"},
            {"name": "Travel", "slug": "travel", "icon": "🏞️"},
            {"name": "Entertainment", "slug": "entertainments", "icon": "🍿"},
            {"name": "Food", "slug": "meal", "icon": "🍴"},
        ]

        category_objects = {}
        for c in categories:
            category, created = Category.objects.get_or_create(
                slug=c["slug"], defaults=c
            )
            category_objects[c["slug"]] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Category created: {category.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Category already exists: {category.name}"))

        # Step 2: Create sports places
        self.stdout.write(self.style.SUCCESS("\n🏃 STEP 2: Creating sports places (15 places)..."))

        sport_places = [
            {
                "name": 'Amirsoy Ski Resort',
                "slug": "amirsoy-ski-resort",
                "category": category_objects["sport"],
                "latitude": 41.4747, "longitude": 70.0882,
                "image": "places/sport/amirsoy.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Chimgan Mountains", 
                "slug": "chimgan-mountains",
                "category": category_objects["sport"], 
                "latitude": 41.5000, "longitude": 70.0833,
                "image": "places/sport/chimgan.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Charvak Reservoir", 
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
                "name": "Yunusabad Sports Complex", 
                "slug": "yunusabad-sports-complex",
                "category": category_objects["sport"], 
                "latitude": 41.3667, "longitude": 69.2833,
                "image": "places/sport/yunusabad.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Tashkent Tennis Court", 
                "slug": "tashkent-tennis-court",
                "category": category_objects["sport"], 
                "latitude": 41.3000, "longitude": 69.2667,
                "image": "places/sport/tennis.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Tashkent Aquapark", 
                "slug": "tashkent-aquapark",
                "category": category_objects["sport"], 
                "latitude": 41.3333, "longitude": 69.2333,
                "image": "places/sport/aquapark.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Alay Climbing Wall", 
                "slug": "alay-climbing-wall",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/sport/climbing.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Mirzo Ulugbek Velodrome", 
                "slug": "mirzo-ulugbek-velodrome",
                "category": category_objects["sport"], 
                "latitude": 41.3500, "longitude": 69.2000,
                "image": "places/sport/velodrome.jpg", "rating": 4.2, "price_range": "$$",
            },
            {
                "name": "Tashkent Golf Club", 
                "slug": "tashkent-golf-club",
                "category": category_objects["sport"], 
                "latitude": 41.2667, "longitude": 69.1833,
                "image": "places/sport/golf.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Premium Fitness Center", 
                "slug": "premium-fitness-center",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/sport/fitness.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Olympic Swimming Pool", 
                "slug": "olympic-swimming-pool",
                "category": category_objects["sport"], 
                "latitude": 41.2833, "longitude": 69.2333,
                "image": "places/sport/pool.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Pakhtakor Stadium", 
                "slug": "pakhtakor-stadium",
                "category": category_objects["sport"], 
                "latitude": 41.3167, "longitude": 69.2667,
                "image": "places/sport/pakhtakor.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Strike Bowling Club", 
                "slug": "strike-bowling-club",
                "category": category_objects["sport"], 
                "latitude": 41.3333, "longitude": 69.2167,
                "image": "places/sport/bowling.jpg", "rating": 4.2, "price_range": "$$",
            },
        ]

        self._create_places(sport_places, "sports")

        # Step 3: Create cultural places
        self.stdout.write(self.style.SUCCESS("\n🎭 STEP 3: Creating cultural places (15 places)..."))

        culture_places = [
            {
                "name": "State Museum of History of Uzbekistan",
                "slug": "state-museum-of-history",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/culture/history_museum.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Alisher Navoi Opera and Ballet Theater",
                "slug": "navoi-theater", 
                "category": category_objects["culture"],
                "latitude": 41.3167, "longitude": 69.2833,
                "image": "places/culture/navoi_theater.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Uzbekistan Museum of Arts", 
                "slug": "art-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2667,
                "image": "places/culture/art_museum.jpg", "rating": 4.4, "price_range": "$",
            },
            {
                "name": "Kukeldash Madrasah", 
                "slug": "kukeldash-madrasah",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2333,
                "image": "places/culture/kukeldash.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "International Forum Palace", 
                "slug": "international-forum-palace",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.3000,
                "image": "places/culture/forum_palace.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Ilhom Theater", 
                "slug": "ilhom-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/culture/ilhom.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Fine Arts Gallery", 
                "slug": "fine-arts-gallery",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.2000,
                "image": "places/culture/gallery.jpg", "rating": 4.2, "price_range": "$",
            },
            {
                "name": "Friendship of Nations Concert Hall", 
                "slug": "friendship-concert-hall",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1833,
                "image": "places/culture/concert_hall.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Puppet Theater", 
                "slug": "puppet-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1667,
                "image": "places/culture/puppet.jpg", "rating": 4.1, "price_range": "$",
            },
            {
                "name": "Museum of Applied Arts", 
                "slug": "applied-arts-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1500,
                "image": "places/culture/applied_arts.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Hamza Drama Theater", 
                "slug": "hamza-drama-theater",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1333,
                "image": "places/culture/drama.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Contemporary Art Center", 
                "slug": "contemporary-art-center",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1167,
                "image": "places/culture/contemporary.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Literature Museum", 
                "slug": "literature-museum",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.1000,
                "image": "places/culture/literature.jpg", "rating": 4.0, "price_range": "$",
            },
            {
                "name": "Uzbekistan Philharmonic", 
                "slug": "uzbekistan-philharmonic",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.0833,
                "image": "places/culture/philharmonic.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "4D Cinema", 
                "slug": "4d-cinema",
                "category": category_objects["culture"], 
                "latitude": 41.3167, "longitude": 69.0667,
                "image": "places/culture/cinema.jpg", "rating": 4.2, "price_range": "$$",
            },
        ]

        self._create_places(culture_places, "cultural")

        # Step 4: Create historical places
        self.stdout.write(self.style.SUCCESS("\n🏛️ STEP 4: Creating historical places (15 places)..."))

        history_places = [
            {
                "name": "Hast-Imam Square", 
                "slug": "hast-imam-square",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2400,
                "image": "places/history/hast_imam.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Kaffal Shashi Mausoleum", 
                "slug": "kaffal-shashi-mausoleum",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2450,
                "image": "places/history/kaffal.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Minor Mosque", 
                "slug": "minor-mosque",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2500,
                "image": "places/history/minor.jpg", "rating": 4.7, "price_range": "$",
            },
            {
                "name": "Hazrati Imam Complex", 
                "slug": "hazrati-imam-complex",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2550,
                "image": "places/history/hazrati.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Barak-Khan Madrasah", 
                "slug": "barak-khan-madrasah",
                "category": category_objects["history"], 
                "latitude": 41.3367, "longitude": 69.2600,
                "image": "places/history/barak.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Zangiata Mausoleum", 
                "slug": "zangiata-mausoleum",
                "category": category_objects["history"], 
                "latitude": 41.1967, "longitude": 69.1450,
                "image": "places/history/zangiata.jpg", "rating": 4.4, "price_range": "$",
            },
            {
                "name": "Afrasiab Settlement", 
                "slug": "afrasiab-settlement",
                "category": category_objects["history"], 
                "latitude": 39.6667, "longitude": 66.9833,
                "image": "places/history/afrasiab.jpg", "rating": 4.7, "price_range": "$",
            },
            {
                "name": "Ulugbek Observatory", 
                "slug": "ulugbek-observatory",
                "category": category_objects["history"], 
                "latitude": 39.6667, "longitude": 66.9667,
                "image": "places/history/ulugbek.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Gur-Emir Mausoleum", 
                "slug": "gur-emir-mausoleum",
                "category": category_objects["history"], 
                "latitude": 39.6500, "longitude": 66.9667,
                "image": "places/history/gur_emir.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Bibi-Khanym Mosque", 
                "slug": "bibi-khanym-mosque",
                "category": category_objects["history"], 
                "latitude": 39.6600, "longitude": 66.9750,
                "image": "places/history/bibi.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Shahi-Zinda", 
                "slug": "shahi-zinda",
                "category": category_objects["history"], 
                "latitude": 39.6633, "longitude": 66.9833,
                "image": "places/history/shahi.jpg", "rating": 4.8, "price_range": "$",
            },
            {
                "name": "Registan Samarkand", 
                "slug": "registan-samarkand",
                "category": category_objects["history"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/history/registan.jpg", "rating": 4.9, "price_range": "$",
            },
            {
                "name": "Ark Fortress", 
                "slug": "ark-fortress",
                "category": category_objects["history"], 
                "latitude": 39.7767, "longitude": 64.4133,
                "image": "places/history/ark.jpg", "rating": 4.5, "price_range": "$",
            },
            {
                "name": "Chashma-Ayub Mausoleum", 
                "slug": "chashma-ayub-mausoleum",
                "category": category_objects["history"], 
                "latitude": 39.7733, "longitude": 64.4167,
                "image": "places/history/chashma.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Bolo-Khauz Mosque", 
                "slug": "bolo-khauz-mosque",
                "category": category_objects["history"], 
                "latitude": 39.7750, "longitude": 64.4150,
                "image": "places/history/bolo.jpg", "rating": 4.4, "price_range": "$",
            },
        ]

        self._create_places(history_places, "historical")

        # Step 5: Create nature places
        self.stdout.write(self.style.SUCCESS("\n🌿 STEP 5: Creating nature places (15 places)..."))

        nature_places = [
            {
                "name": "Botanical Garden", 
                "slug": "botanical-garden",
                "category": category_objects["nature"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/nature/botanical.jpg", "rating": 4.6, "price_range": "$",
            },
            {
                "name": "Yangiobod", 
                "slug": "yangiobod",
                "category": category_objects["nature"], 
                "latitude": 41.1167, "longitude": 69.9167,
                "image": "places/nature/yangiobod.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Ugam-Chatkal National Park", 
                "slug": "ugam-chatkal-national-park",
                "category": category_objects["nature"], 
                "latitude": 41.5000, "longitude": 70.0833,
                "image": "places/nature/ugam.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Nuratau Mountains", 
                "slug": "nuratau-mountains",
                "category": category_objects["nature"], 
                "latitude": 40.5000, "longitude": 66.6667,
                "image": "places/nature/nuratau.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Aydarkul Lake", 
                "slug": "aydarkul-lake",
                "category": category_objects["nature"], 
                "latitude": 40.9167, "longitude": 66.8333,
                "image": "places/nature/aydarkul.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Pulathan Plateau", 
                "slug": "pulathan-plateau",
                "category": category_objects["nature"], 
                "latitude": 41.0833, "longitude": 70.1667,
                "image": "places/nature/pulathan.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Arslanbob Waterfall", 
                "slug": "arslanbob-waterfall",
                "category": category_objects["nature"], 
                "latitude": 41.3333, "longitude": 72.4333,
                "image": "places/nature/arslanbob.jpg", "rating": 4.9, "price_range": "$$",
            },
            {
                "name": "Sayrok Lakes", 
                "slug": "sayrok-lakes",
                "category": category_objects["nature"], 
                "latitude": 41.2500, "longitude": 70.1667,
                "image": "places/nature/sayrok.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Sangardak Canyon", 
                "slug": "sangardak-canyon",
                "category": category_objects["nature"], 
                "latitude": 38.2500, "longitude": 67.9000,
                "image": "places/nature/sangardak.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Kyzylkum Reserve", 
                "slug": "kyzylkum-reserve",
                "category": category_objects["nature"], 
                "latitude": 42.0000, "longitude": 63.0000,
                "image": "places/nature/kyzylkum.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Big Chimgan Mountain", 
                "slug": "big-chimgan-mountain",
                "category": category_objects["nature"], 
                "latitude": 41.4833, "longitude": 70.0333,
                "image": "places/nature/big_chimgan.jpg", "rating": 4.8, "price_range": "$$",
            },
            {
                "name": "Amankutan Gorge", 
                "slug": "amankutan-gorge",
                "category": category_objects["nature"], 
                "latitude": 39.4167, "longitude": 67.0333,
                "image": "places/nature/amankutan.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Tudakul Lake", 
                "slug": "tudakul-lake",
                "category": category_objects["nature"], 
                "latitude": 40.0833, "longitude": 64.6333,
                "image": "places/nature/tudakul.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Nurata Reserve", 
                "slug": "nurata-reserve",
                "category": category_objects["nature"], 
                "latitude": 40.5000, "longitude": 66.6667,
                "image": "places/nature/nurata.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Hissar Range", 
                "slug": "hissar-range",
                "category": category_objects["nature"], 
                "latitude": 38.5000, "longitude": 68.0000,
                "image": "places/nature/hissar.jpg", "rating": 4.6, "price_range": "$$",
            },
        ]

        self._create_places(nature_places, "nature")

        # Step 6: Create travel places
        self.stdout.write(self.style.SUCCESS("\n🏞️ STEP 6: Creating travel places (15 places)..."))

        travel_places = [
            {
                "name": "Road to Chimgan", 
                "slug": "road-to-chimgan",
                "category": category_objects["travel"], 
                "latitude": 41.4000, "longitude": 69.9167,
                "image": "places/travel/chimgan_road.jpg", "rating": 4.7, "price_range": "$$",
            },
            {
                "name": "Ancient Cities Tour", 
                "slug": "ancient-cities-tour",
                "category": category_objects["travel"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/travel/ancient_tour.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Tashkent Excursion", 
                "slug": "tashkent-excursion",
                "category": category_objects["travel"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/travel/tashkent_tour.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Nurata Journey", 
                "slug": "nurata-journey",
                "category": category_objects["travel"], 
                "latitude": 40.5000, "longitude": 65.6667,
                "image": "places/travel/nurata_tour.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Fergana Valley Tour", 
                "slug": "fergana-valley-tour",
                "category": category_objects["travel"], 
                "latitude": 40.3864, "longitude": 71.7864,
                "image": "places/travel/fergana.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Kyzylkum Expedition", 
                "slug": "kyzylkum-expedition",
                "category": category_objects["travel"], 
                "latitude": 42.0000, "longitude": 63.5000,
                "image": "places/travel/kyzylkum_exp.jpg", "rating": 4.4, "price_range": "$$$",
            },
            {
                "name": "Silk Road Tour", 
                "slug": "silk-road-tour",
                "category": category_objects["travel"], 
                "latitude": 40.1000, "longitude": 67.8333,
                "image": "places/travel/silk_road.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Aral Sea Journey", 
                "slug": "aral-sea-journey",
                "category": category_objects["travel"], 
                "latitude": 45.0000, "longitude": 59.0000,
                "image": "places/travel/aral.jpg", "rating": 4.3, "price_range": "$$$",
            },
            {
                "name": "Khorezm Tour", 
                "slug": "khorezm-tour",
                "category": category_objects["travel"], 
                "latitude": 41.5500, "longitude": 60.6333,
                "image": "places/travel/khorezm.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Shahrisabz Excursion", 
                "slug": "shahrisabz-excursion",
                "category": category_objects["travel"], 
                "latitude": 39.0578, "longitude": 66.8342,
                "image": "places/travel/shahrisabz.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Bukhara Tour", 
                "slug": "bukhara-tour",
                "category": category_objects["travel"], 
                "latitude": 39.7667, "longitude": 64.4167,
                "image": "places/travel/bukhara.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Termez Journey", 
                "slug": "termez-journey",
                "category": category_objects["travel"], 
                "latitude": 37.2242, "longitude": 67.2783,
                "image": "places/travel/termez.jpg", "rating": 4.5, "price_range": "$$$",
            },
            {
                "name": "Zaamin Ecotourism", 
                "slug": "zaamin-ecotourism",
                "category": category_objects["travel"], 
                "latitude": 39.9667, "longitude": 68.4000,
                "image": "places/travel/zaamin.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Samarkand Tour", 
                "slug": "samarkand-tour",
                "category": category_objects["travel"], 
                "latitude": 39.6547, "longitude": 66.9750,
                "image": "places/travel/samarkand_tour.jpg", "rating": 4.9, "price_range": "$$$",
            },
            {
                "name": "Karshi Journey", 
                "slug": "karshi-journey",
                "category": category_objects["travel"], 
                "latitude": 38.8667, "longitude": 65.8000,
                "image": "places/travel/karshi.jpg", "rating": 4.4, "price_range": "$$",
            },
        ]

        self._create_places(travel_places, "travel")

        # Step 7: Create entertainment places
        self.stdout.write(self.style.SUCCESS("\n🍿 STEP 7: Creating entertainment places (15 places)..."))

        entertainment_places = [
            {
                "name": "Ashgabat Park", 
                "slug": "ashgabat-park",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2833,
                "image": "places/entertainment/ashgabat.jpg", "rating": 4.3, "price_range": "$",
            },
            {
                "name": "Next Entertainment Center", 
                "slug": "next-entertainment-center",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2500,
                "image": "places/entertainment/next.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Star Cinema", 
                "slug": "star-cinema",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2333,
                "image": "places/entertainment/star.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "Luna Park", 
                "slug": "luna-park",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2167,
                "image": "places/entertainment/luna.jpg", "rating": 4.2, "price_range": "$$",
            },
            {
                "name": "Victory Bowling Club", 
                "slug": "victory-bowling",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.2000,
                "image": "places/entertainment/victory.jpg", "rating": 4.3, "price_range": "$$",
            },
            {
                "name": "Melody Karaoke Club", 
                "slug": "melody-karaoke",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1833,
                "image": "places/entertainment/melody.jpg", "rating": 4.6, "price_range": "$$",
            },
            {
                "name": "Champion Billiards Club", 
                "slug": "champion-billiards",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1667,
                "image": "places/entertainment/champion.jpg", "rating": 4.4, "price_range": "$$",
            },
            {
                "name": "GameZone Arcade", 
                "slug": "gamezone-arcade",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1500,
                "image": "places/entertainment/gamezone.jpg", "rating": 4.5, "price_range": "$$",
            },
            {
                "name": "Samarkand Darvoza Mall", 
                "slug": "samarkand-darvoza-mall",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1333,
                "image": "places/entertainment/darvoza.jpg", "rating": 4.7, "price_range": "$$$",
            },
            {
                "name": "Magic City Complex", 
                "slug": "magic-city-complex",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1167,
                "image": "places/entertainment/magic.jpg", "rating": 4.8, "price_range": "$$$",
            },
            {
                "name": "Escape Quest Room", 
                "slug": "escape-quest-room",
                "category": category_objects["entertainments"], 
                "latitude": 41.3167, "longitude": 69.1000,
                "