# Local Nutrition Database for Food-101 and COCO Food categories
# Values are approximate per 100g

NUTRITION_DATABASE = {
    # COCO Ingredients (YOLO classes)
    "apple": {"name": "Apple", "calories": 52, "protein": 0.3, "carbs": 14.0, "fat": 0.2, "serving_size": 150},
    "banana": {"name": "Banana", "calories": 89, "protein": 1.1, "carbs": 23.0, "fat": 0.3, "serving_size": 120},
    "orange": {"name": "Orange", "calories": 47, "protein": 0.9, "carbs": 12.0, "fat": 0.1, "serving_size": 130},
    "broccoli": {"name": "Broccoli", "calories": 34, "protein": 2.8, "carbs": 7.0, "fat": 0.4, "serving_size": 85},
    "carrot": {"name": "Carrot", "calories": 41, "protein": 0.9, "carbs": 10.0, "fat": 0.2, "serving_size": 75},
    "sandwich": {"name": "Sandwich", "calories": 250, "protein": 12.0, "carbs": 30.0, "fat": 8.0, "serving_size": 180},
    "hot dog": {"name": "Hot Dog", "calories": 290, "protein": 10.0, "carbs": 26.0, "fat": 16.0, "serving_size": 120},
    "pizza": {"name": "Pizza Slice", "calories": 266, "protein": 11.0, "carbs": 33.0, "fat": 10.0, "serving_size": 107},
    "donut": {"name": "Donut", "calories": 452, "protein": 4.9, "carbs": 51.0, "fat": 25.0, "serving_size": 60},
    "cake": {"name": "Slice of Cake", "calories": 371, "protein": 5.3, "carbs": 53.0, "fat": 15.0, "serving_size": 80},

    # Food-101 Dishes
    "apple_pie": {"name": "Apple Pie", "calories": 237, "protein": 1.9, "carbs": 34.0, "fat": 11.0, "serving_size": 125},
    "baby_back_ribs": {"name": "Baby Back Ribs", "calories": 282, "protein": 20.0, "carbs": 0.0, "fat": 22.0, "serving_size": 250},
    "baklava": {"name": "Baklava", "calories": 428, "protein": 6.0, "carbs": 53.0, "fat": 22.0, "serving_size": 70},
    "beef_carpaccio": {"name": "Beef Carpaccio", "calories": 160, "protein": 22.0, "carbs": 1.0, "fat": 8.0, "serving_size": 120},
    "beef_tartare": {"name": "Beef Tartare", "calories": 146, "protein": 19.0, "carbs": 1.5, "fat": 7.0, "serving_size": 150},
    "beet_salad": {"name": "Beet Salad", "calories": 110, "protein": 2.0, "carbs": 9.0, "fat": 8.0, "serving_size": 150},
    "beignets": {"name": "Beignets", "calories": 380, "protein": 6.0, "carbs": 50.0, "fat": 17.0, "serving_size": 85},
    "bibimbap": {"name": "Bibimbap", "calories": 135, "protein": 5.5, "carbs": 20.0, "fat": 3.5, "serving_size": 400},
    "bread_pudding": {"name": "Bread Pudding", "calories": 270, "protein": 5.0, "carbs": 42.0, "fat": 9.0, "serving_size": 150},
    "bruschetta": {"name": "Bruschetta", "calories": 150, "protein": 4.0, "carbs": 20.0, "fat": 6.0, "serving_size": 80},
    "caesar_salad": {"name": "Caesar Salad", "calories": 140, "protein": 3.0, "carbs": 8.0, "fat": 11.0, "serving_size": 200},
    "caprese_salad": {"name": "Caprese Salad", "calories": 150, "protein": 6.5, "carbs": 3.0, "fat": 13.0, "serving_size": 150},
    "carrot_cake": {"name": "Carrot Cake", "calories": 326, "protein": 3.5, "carbs": 44.0, "fat": 16.0, "serving_size": 100},
    "ceviche": {"name": "Ceviche", "calories": 98, "protein": 14.0, "carbs": 4.0, "fat": 2.0, "serving_size": 180},
    "cheesecake": {"name": "Cheesecake", "calories": 321, "protein": 5.5, "carbs": 26.0, "fat": 23.0, "serving_size": 100},
    "cheese_plate": {"name": "Cheese Plate", "calories": 380, "protein": 22.0, "carbs": 2.0, "fat": 32.0, "serving_size": 150},
    "chicken_curry": {"name": "Chicken Curry", "calories": 110, "protein": 11.0, "carbs": 8.0, "fat": 4.0, "serving_size": 300},
    "chicken_quesadilla": {"name": "Chicken Quesadilla", "calories": 251, "protein": 14.0, "carbs": 22.0, "fat": 12.0, "serving_size": 200},
    "chicken_wings": {"name": "Chicken Wings", "calories": 290, "protein": 20.0, "carbs": 0.0, "fat": 20.0, "serving_size": 180},
    "chocolate_cake": {"name": "Chocolate Cake", "calories": 371, "protein": 4.1, "carbs": 53.0, "fat": 16.0, "serving_size": 100},
    "chocolate_mousse": {"name": "Chocolate Mousse", "calories": 225, "protein": 4.0, "carbs": 21.0, "fat": 15.0, "serving_size": 90},
    "churros": {"name": "Churros", "calories": 383, "protein": 4.5, "carbs": 48.0, "fat": 20.0, "serving_size": 90},
    "clam_chowder": {"name": "Clam Chowder", "calories": 86, "protein": 4.5, "carbs": 9.0, "fat": 3.5, "serving_size": 240},
    "club_sandwich": {"name": "Club Sandwich", "calories": 233, "protein": 13.0, "carbs": 18.0, "fat": 12.0, "serving_size": 220},
    "crab_cakes": {"name": "Crab Cakes", "calories": 220, "protein": 15.0, "carbs": 12.0, "fat": 12.0, "serving_size": 150},
    "creme_brulee": {"name": "Creme Brulee", "calories": 331, "protein": 4.0, "carbs": 26.0, "fat": 24.0, "serving_size": 100},
    "croque_madame": {"name": "Croque Madame", "calories": 280, "protein": 15.0, "carbs": 22.0, "fat": 14.0, "serving_size": 200},
    "cup_cakes": {"name": "Cupcake", "calories": 380, "protein": 3.0, "carbs": 52.0, "fat": 18.0, "serving_size": 70},
    "deviled_eggs": {"name": "Deviled Eggs", "calories": 200, "protein": 12.0, "carbs": 2.0, "fat": 16.0, "serving_size": 100},
    "donuts": {"name": "Donuts", "calories": 452, "protein": 4.9, "carbs": 51.0, "fat": 25.0, "serving_size": 60},
    "dumplings": {"name": "Dumplings", "calories": 150, "protein": 7.0, "carbs": 20.0, "fat": 4.5, "serving_size": 150},
    "edamame": {"name": "Edamame", "calories": 122, "protein": 11.0, "carbs": 10.0, "fat": 5.0, "serving_size": 100},
    "eggs_benedict": {"name": "Eggs Benedict", "calories": 230, "protein": 12.0, "carbs": 13.0, "fat": 15.0, "serving_size": 180},
    "escargots": {"name": "Escargots", "calories": 150, "protein": 16.0, "carbs": 5.0, "fat": 8.0, "serving_size": 100},
    "falafel": {"name": "Falafel", "calories": 333, "protein": 13.0, "carbs": 32.0, "fat": 18.0, "serving_size": 150},
    "filet_mignon": {"name": "Filet Mignon", "calories": 220, "protein": 26.0, "carbs": 0.0, "fat": 12.0, "serving_size": 200},
    "fish_and_chips": {"name": "Fish and Chips", "calories": 195, "protein": 10.0, "carbs": 21.0, "fat": 8.0, "serving_size": 300},
    "foie_gras": {"name": "Foie Gras", "calories": 462, "protein": 11.0, "carbs": 5.0, "fat": 44.0, "serving_size": 50},
    "french_fries": {"name": "French Fries", "calories": 312, "protein": 3.4, "carbs": 41.0, "fat": 15.0, "serving_size": 117},
    "french_onion_soup": {"name": "French Onion Soup", "calories": 55, "protein": 3.0, "carbs": 6.0, "fat": 2.2, "serving_size": 250},
    "french_toast": {"name": "French Toast", "calories": 229, "protein": 6.0, "carbs": 26.0, "fat": 11.0, "serving_size": 130},
    "fried_calamari": {"name": "Fried Calamari", "calories": 250, "protein": 15.0, "carbs": 18.0, "fat": 13.0, "serving_size": 150},
    "fried_rice": {"name": "Fried Rice", "calories": 163, "protein": 4.0, "carbs": 28.0, "fat": 4.0, "serving_size": 250},
    "frozen_yogurt": {"name": "Frozen Yogurt", "calories": 159, "protein": 4.0, "carbs": 24.0, "fat": 5.6, "serving_size": 120},
    "garlic_bread": {"name": "Garlic Bread", "calories": 350, "protein": 8.0, "carbs": 44.0, "fat": 16.0, "serving_size": 60},
    "gnocchi": {"name": "Gnocchi", "calories": 133, "protein": 3.5, "carbs": 28.0, "fat": 0.5, "serving_size": 200},
    "greek_salad": {"name": "Greek Salad", "calories": 115, "protein": 2.5, "carbs": 6.0, "fat": 9.5, "serving_size": 200},
    "grilled_cheese_sandwich": {"name": "Grilled Cheese Sandwich", "calories": 320, "protein": 11.0, "carbs": 33.0, "fat": 16.0, "serving_size": 116},
    "grilled_salmon": {"name": "Grilled Salmon", "calories": 206, "protein": 22.0, "carbs": 0.0, "fat": 12.0, "serving_size": 150},
    "guacamole": {"name": "Guacamole", "calories": 157, "protein": 2.0, "carbs": 9.0, "fat": 15.0, "serving_size": 50},
    "gyoza": {"name": "Gyoza", "calories": 180, "protein": 8.0, "carbs": 22.0, "fat": 6.0, "serving_size": 150},
    "hamburger": {"name": "Hamburger", "calories": 254, "protein": 13.0, "carbs": 24.0, "fat": 12.0, "serving_size": 200},
    "hot_and_sour_soup": {"name": "Hot and Sour Soup", "calories": 45, "protein": 2.5, "carbs": 6.0, "fat": 1.2, "serving_size": 240},
    "hot_dog": {"name": "Hot Dog", "calories": 290, "protein": 10.0, "carbs": 26.0, "fat": 16.0, "serving_size": 120},
    "huevos_rancheros": {"name": "Huevos Rancheros", "calories": 180, "protein": 8.0, "carbs": 16.0, "fat": 9.0, "serving_size": 250},
    "hummus": {"name": "Hummus", "calories": 166, "protein": 8.0, "carbs": 14.0, "fat": 10.0, "serving_size": 60},
    "ice_cream": {"name": "Ice Cream", "calories": 207, "protein": 3.5, "carbs": 24.0, "fat": 11.0, "serving_size": 100},
    "lasagna": {"name": "Lasagna", "calories": 135, "protein": 8.0, "carbs": 12.0, "fat": 6.0, "serving_size": 350},
    "lobster_roll_sandwich": {"name": "Lobster Roll Sandwich", "calories": 240, "protein": 16.0, "carbs": 20.0, "fat": 10.0, "serving_size": 180},
    "lobster_bisque": {"name": "Lobster Bisque", "calories": 112, "protein": 5.0, "carbs": 8.0, "fat": 7.0, "serving_size": 240},
    "macaroni_and_cheese": {"name": "Macaroni & Cheese", "calories": 164, "protein": 7.0, "carbs": 20.0, "fat": 6.0, "serving_size": 200},
    "macarons": {"name": "Macarons", "calories": 460, "protein": 7.0, "carbs": 58.0, "fat": 22.0, "serving_size": 40},
    "miso_soup": {"name": "Miso Soup", "calories": 36, "protein": 2.0, "carbs": 5.0, "fat": 1.0, "serving_size": 240},
    "mussels": {"name": "Mussels", "calories": 172, "protein": 24.0, "carbs": 7.0, "fat": 4.5, "serving_size": 150},
    "nachos": {"name": "Nachos", "calories": 306, "protein": 8.0, "carbs": 33.0, "fat": 16.0, "serving_size": 200},
    "omelette": {"name": "Omelette", "calories": 154, "protein": 11.0, "carbs": 0.6, "fat": 12.0, "serving_size": 150},
    "onion_rings": {"name": "Onion Rings", "calories": 411, "protein": 4.0, "carbs": 44.0, "fat": 24.0, "serving_size": 100},
    "oysters": {"name": "Oysters", "calories": 81, "protein": 9.0, "carbs": 5.0, "fat": 2.5, "serving_size": 100},
    "pad_thai": {"name": "Pad Thai", "calories": 186, "protein": 7.0, "carbs": 32.0, "fat": 3.5, "serving_size": 350},
    "paella": {"name": "Paella", "calories": 156, "protein": 9.0, "carbs": 24.0, "fat": 2.5, "serving_size": 350},
    "pancakes": {"name": "Pancakes", "calories": 227, "protein": 6.0, "carbs": 28.0, "fat": 10.0, "serving_size": 150},
    "panna_cotta": {"name": "Panna Cotta", "calories": 220, "protein": 3.0, "carbs": 22.0, "fat": 13.0, "serving_size": 120},
    "peking_duck": {"name": "Peking Duck", "calories": 337, "protein": 19.0, "carbs": 0.0, "fat": 28.0, "serving_size": 200},
    "pho": {"name": "Pho", "calories": 75, "protein": 6.0, "carbs": 10.0, "fat": 1.2, "serving_size": 400},
    "pizza_dish": {"name": "Pizza", "calories": 266, "protein": 11.0, "carbs": 33.0, "fat": 10.0, "serving_size": 300},  # duplicate fallback name
    "pork_chop": {"name": "Pork Chop", "calories": 231, "protein": 24.0, "carbs": 0.0, "fat": 14.0, "serving_size": 180},
    "poutine": {"name": "Poutine", "calories": 170, "protein": 5.0, "carbs": 18.0, "fat": 9.0, "serving_size": 250},
    "prime_rib": {"name": "Prime Rib", "calories": 350, "protein": 22.0, "carbs": 0.0, "fat": 29.0, "serving_size": 250},
    "pulled_pork_sandwich": {"name": "Pulled Pork Sandwich", "calories": 240, "protein": 14.0, "carbs": 22.0, "fat": 10.0, "serving_size": 200},
    "ramen": {"name": "Ramen", "calories": 85, "protein": 4.0, "carbs": 12.0, "fat": 2.5, "serving_size": 450},
    "ravioli": {"name": "Ravioli", "calories": 167, "protein": 6.5, "carbs": 25.0, "fat": 4.5, "serving_size": 200},
    "red_velvet_cake": {"name": "Red Velvet Cake", "calories": 367, "protein": 3.7, "carbs": 53.0, "fat": 15.0, "serving_size": 100},
    "risotto": {"name": "Risotto", "calories": 143, "protein": 3.5, "carbs": 22.0, "fat": 4.5, "serving_size": 250},
    "samosa": {"name": "Samosa", "calories": 262, "protein": 4.5, "carbs": 32.0, "fat": 13.0, "serving_size": 80},
    "sashimi": {"name": "Sashimi", "calories": 120, "protein": 20.0, "carbs": 0.5, "fat": 4.0, "serving_size": 120},
    "scallops": {"name": "Scallops", "calories": 111, "protein": 20.0, "carbs": 5.0, "fat": 1.0, "serving_size": 150},
    "seaweed_salad": {"name": "Seaweed Salad", "calories": 90, "protein": 1.5, "carbs": 12.0, "fat": 4.5, "serving_size": 100},
    "shrimp_and_grits": {"name": "Shrimp and Grits", "calories": 160, "protein": 10.0, "carbs": 18.0, "fat": 5.0, "serving_size": 300},
    "spaghetti_bolognese": {"name": "Spaghetti Bolognese", "calories": 140, "protein": 7.0, "carbs": 19.0, "fat": 4.0, "serving_size": 300},
    "spaghetti_carbonara": {"name": "Spaghetti Carbonara", "calories": 220, "protein": 10.0, "carbs": 24.0, "fat": 9.0, "serving_size": 300},
    "spring_rolls": {"name": "Spring Rolls", "calories": 150, "protein": 4.0, "carbs": 20.0, "fat": 6.0, "serving_size": 120},
    "steak": {"name": "Steak", "calories": 252, "protein": 27.3, "carbs": 0.0, "fat": 15.0, "serving_size": 200},
    "strawberry_shortcake": {"name": "Strawberry Shortcake", "calories": 280, "protein": 3.5, "carbs": 44.0, "fat": 10.0, "serving_size": 120},
    "sushi": {"name": "Sushi", "calories": 130, "protein": 6.0, "carbs": 24.0, "fat": 1.0, "serving_size": 180},
    "tacos": {"name": "Tacos", "calories": 226, "protein": 11.0, "carbs": 20.0, "fat": 11.0, "serving_size": 150},
    "takoyaki": {"name": "Takoyaki", "calories": 180, "protein": 6.0, "carbs": 24.0, "fat": 6.5, "serving_size": 150},
    "tiramisu": {"name": "Tiramisu", "calories": 354, "protein": 5.5, "carbs": 38.0, "fat": 20.0, "serving_size": 90},
    "tuna_tartare": {"name": "Tuna Tartare", "calories": 130, "protein": 22.0, "carbs": 2.0, "fat": 3.0, "serving_size": 150},
    "waffles": {"name": "Waffles", "calories": 291, "protein": 6.0, "carbs": 33.0, "fat": 15.0, "serving_size": 100},
}

# Alias mapping from model class name formatting to NUTRITION_DATABASE keys
CLASS_ALIASES = {
    "pizza_dish": "pizza",
}

def get_nutrition_data(food_class: str) -> dict:
    normalized = food_class.lower().strip()
    # Apply aliases
    normalized = CLASS_ALIASES.get(normalized, normalized)
    
    # Try finding in database
    if normalized in NUTRITION_DATABASE:
        return NUTRITION_DATABASE[normalized]
        
    # Match snake_case variants
    under_normalized = normalized.replace(" ", "_")
    if under_normalized in NUTRITION_DATABASE:
        return NUTRITION_DATABASE[under_normalized]
        
    # Standard default fallback
    readable_name = food_class.replace("_", " ").title()
    return {
        "name": readable_name,
        "calories": 150,
        "protein": 5.0,
        "carbs": 20.0,
        "fat": 5.0,
        "serving_size": 100
    }
