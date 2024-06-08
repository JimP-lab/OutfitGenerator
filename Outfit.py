import random

# Function to generate random outfit suggestions
def suggest_outfit():
    outfits = [
        "You should wear a blue dress with white sneakers.",
        "Try a striped shirt with jeans and boots.",
        "A floral skirt with a plain t-shirt would look great.",
        "Pair a leather jacket with black leggings and ankle boots.",
        "How about a button-down shirt with chinos and loafers?"
    ]
    return random.choice(outfits)

# Function to generate placeholder outfit image URLs
def generate_outfit_image():
    # Placeholder code: Replace this with your image generation logic
    return "https://example.com/outfit.jpg"

# User preferences
preferences = input("Enter your outfit preferences: ")

# Generate random outfit suggestion
outfit_suggestion = suggest_outfit()

# Generate outfit image URL
outfit_image_url = generate_outfit_image()

# Display outfit suggestion and image URL
print("Outfit Suggestion:", outfit_suggestion)
print("Outfit Image URL:", outfit_image_url)


