# Appliance presets and cost calculation

APPLIANCE_PRESETS = {
    "Refrigerator": {"watts": "150W", "usage": "24", "rate": "12"},
    "Television": {"watts": "100W", "usage": "4", "rate": "12"},
    "Air Conditioner": {"watts": "1200W", "usage": "8", "rate": "12"},
    "Electric Fan": {"watts": "75W", "usage": "6", "rate": "12"},
    "Light Bulb": {"watts": "10W", "usage": "5", "rate": "12"},
    "Washing Machine": {"watts": "500W", "usage": "1", "rate": "12"},
    "Microwave Oven": {"watts": "1000W", "usage": "0.5", "rate": "12"},
    "Electric Kettle": {"watts": "1500W", "usage": "0.3", "rate": "12"},
    "Rice Cooker": {"watts": "700W", "usage": "1", "rate": "12"},
    "Hair Dryer": {"watts": "1200W", "usage": "0.2", "rate": "12"},
    "Desktop Computer": {"watts": "250W", "usage": "6", "rate": "12"},
    "Laptop": {"watts": "60W", "usage": "6", "rate": "12"},
    "Wi-Fi Router": {"watts": "10W", "usage": "24", "rate": "12"},
    "Electric Iron": {"watts": "1000W", "usage": "0.5", "rate": "12"},
    "Blender": {"watts": "300W", "usage": "0.2", "rate": "12"},
    "Toaster": {"watts": "800W", "usage": "0.2", "rate": "12"},
    "Water Dispenser": {"watts": "100W", "usage": "8", "rate": "12"},
    "Printer": {"watts": "50W", "usage": "0.5", "rate": "12"},
}

def calculate_cost(entry: str) -> float:
    """Parse an appliance entry and return daily cost"""
    try:
        parts = entry.split(" - ")[1].split(" x ")
        watts = float(parts[0].replace("W","").strip())
        usage_hr = float(parts[1].split("hr")[0])
        rate = float(parts[1].split("@ ")[1].replace("₱/kWh",""))
        kwh = (watts / 1000) * usage_hr
        return kwh * rate
    except Exception:
        return 0
