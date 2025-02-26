import tkinter as tk
from tkinter import messagebox

def recommend_crop():
    try:
        # Get user inputs
        temperature = float(temp_entry.get())
        rainfall = float(rain_entry.get())
        soil_type = soil_var.get()
        altitude = float(alt_entry.get())
        
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
        if soil_type == "Loamy":
            recommendations.append("Vegetables")
        elif soil_type == "Clayey":
            recommendations.append("Wheat")
        elif soil_type == "Sandy":
            recommendations.append("Cassava")

        # Altitude-based recommendations
        if altitude > 2000:
            recommendations.append("Pyrethrum")
        elif 1000 <= altitude <= 2000:
            recommendations.append("Coffee")
        elif altitude < 1000:
            recommendations.append("Bananas")
        
        # Display recommendations
        result_text.set("Recommended Crops: " + ", ".join(recommendations))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Agricultural Crop Recommendation System")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Heading
tk.Label(root, text="Crop Recommendation System", font=("Arial", 16, "bold"), bg="#228B22", fg="white").pack(fill=tk.X)

# Temperature input
tk.Label(root, text="Temperature (°C):", font=("Arial", 12), bg="#f4f4f4").pack()
temp_entry = tk.Entry(root, font=("Arial", 12))
temp_entry.pack()

# Rainfall input
tk.Label(root, text="Rainfall (mm):", font=("Arial", 12), bg="#f4f4f4").pack()
rain_entry = tk.Entry(root, font=("Arial", 12))
rain_entry.pack()

# Soil Type dropdown
soil_var = tk.StringVar(value="Loamy")
tk.Label(root, text="Soil Type:", font=("Arial", 12), bg="#f4f4f4").pack()
tk.OptionMenu(root, soil_var, "Loamy", "Clayey", "Sandy").pack()

# Altitude input
tk.Label(root, text="Altitude (m):", font=("Arial", 12), bg="#f4f4f4").pack()
alt_entry = tk.Entry(root, font=("Arial", 12))
alt_entry.pack()

# Button to recommend crop
tk.Button(root, text="Get Recommendation", font=("Arial", 14, "bold"), bg="#228B22", fg="white", command=recommend_crop).pack(pady=10)

# Result display
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12, "bold"), fg="black", wraplength=400, bg="#f4f4f4").pack()

# Run the application
root.mainloop()

