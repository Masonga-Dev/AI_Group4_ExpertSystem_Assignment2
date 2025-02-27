from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def recommend_crop(temperature, rainfall, soil_type, altitude):
    recommendations = []

    # Temperature-based recommendations
    if 20 <= temperature <= 30:
        recommendations.append("Maize")
    if 15 <= temperature <= 25:
        recommendations.append("Potatoes")
    if temperature > 30:
        recommendations.append("Sorghum")

    # Rainfall-based recommendations
    if 600 <= rainfall <= 1200:
        recommendations.append("Beans")
    if rainfall > 1200:
        recommendations.append("Rice")
    if rainfall < 600:
        recommendations.append("Millet")

    # Soil Type-based recommendations
    if soil_type.lower() == "loamy":
        recommendations.append("Vegetables")
    elif soil_type.lower() == "clayey":
        recommendations.append("Wheat")
    elif soil_type.lower() == "sandy":
        recommendations.append("Cassava")

    # Altitude-based recommendations
    if altitude > 2000:
        recommendations.append("Pyrethrum")
    elif 1000 <= altitude <= 2000:
        recommendations.append("Coffee")
    elif altitude < 1000:
        recommendations.append("Bananas")
    
    return recommendations if recommendations else ["No suitable crop found"]

def get_input():
    try:
        temperature = float(input("Enter the temperature (°C): "))
        rainfall = float(input("Enter the annual rainfall (mm): "))
        soil_type = input("Enter the soil type (loamy/clayey/sandy): ")
        altitude = float(input("Enter the altitude (meters): "))
        
        recommendations = recommend_crop(temperature, rainfall, soil_type, altitude)
        
        # Design the output with color and style
        print(Fore.GREEN + "\nRecommended crops based on the input:")
        for crop in recommendations:
            print(Fore.CYAN + f"- {crop}")
        
    except ValueError:
        print(Fore.RED + "Please enter valid numeric values for temperature, rainfall, and altitude.")

if __name__ == '__main__':
    get_input()
