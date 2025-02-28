from flask import Flask, render_template, request
from flask_cors import CORS  # Allow Binder access

app = Flask(__name__)
CORS(app)  # Enable CORS for Binder access

def recommend_crop(temperature, rainfall, soil_type, altitude):
    recommendations = []

    # Temperature-based recommendations
    if 20 <= temperature <= 30:
        recommendations.append("Maize")
    if 15 <= temperature <= 25:
        recommendations.append("Potatoes")
    if temperature > 30:
        recommendations.append("Sorghum")  # Fixed typo

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            temperature = float(request.form['temperature'])
            rainfall = float(request.form['rainfall'])
            soil_type = request.form['soil_type']
            altitude = float(request.form['altitude'])
            recommendations = recommend_crop(temperature, rainfall, soil_type, altitude)
            return render_template('index.html', recommendations=recommendations)
        except ValueError:
            return render_template('index.html', error="Please enter valid numeric values.")
    return render_template('index.html')

if __name__ == '__main__':
app.run(host="0.0.0.0", port=5000, debug=True)

