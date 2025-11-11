# utils.py

"""
Contains non-UI logic for calculations and file I/O.
"""
import os

def calculate_total_cost(appliance_items_list):
    """
    Parses a list of appliance strings and calculates the total daily cost.
    
    Args:
        appliance_items_list (list): List of strings, e.g.,
            ["Appliance - 100W x 2hr @ 12₱/kWh"]

    Returns:
        float: The total daily cost.
        
    Raises:
        ValueError: If parsing fails for any item.
    """
    total_cost = 0.0
    for item_text in appliance_items_list:
        try:
            # "Appliance - 100W x 2hr @ 12₱/kWh"
            parts = item_text.split(" - ")[1].split(" x ")
            # parts[0] = "100W"
            watts = float(parts[0].replace("W", "").strip())
            
            # parts[1] = "2hr @ 12₱/kWh"
            usage_parts = parts[1].split(" @ ")
            # usage_parts[0] = "2hr"
            usage_hr = float(usage_parts[0].replace("hr", ""))
            
            # usage_parts[1] = "12₱/kWh"
            rate = float(usage_parts[1].replace("₱/kWh", ""))
            
            kwh = (watts / 1000) * usage_hr
            cost = kwh * rate
            total_cost += cost
        except Exception as e:
            raise ValueError(f"Failed to parse item: {item_text}\nError: {e}")
    
    return total_cost


def save_calculation_history(user, items_list, daily_cost, monthly_cost):
    """
    Saves the calculation results to a user-specific history file.
    """
    if not user:
        return
        
    try:
        user_dir = os.path.join(os.getcwd(), "users", user)
        os.makedirs(user_dir, exist_ok=True)
        history_path = os.path.join(user_dir, "history.txt")
        
        with open(history_path, "a", encoding="utf-8") as f:
            f.write("---- New Calculation ----\n")
            for item in items_list:
                f.write(item + "\n")
            f.write(f"Total Daily: ₱{daily_cost:.2f}, Monthly: ₱{monthly_cost:.2f}\n\n")
            
    except Exception as e:
        print(f"Error saving history: {e}") # Log to console instead of showing a popup