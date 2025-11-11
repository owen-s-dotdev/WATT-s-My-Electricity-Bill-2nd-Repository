# logic.py

"""
Contains the business logic for calculations and file I/O.
"""
import os

def calculate_total_cost(items):
    """
    Calculates the total daily and monthly cost from a list of appliance strings.
    
    Args:
        items (list[str]): A list of strings from the appliance combo box.
        
    Returns:
        tuple: (total_daily_cost, monthly_cost, error_message)
               On success, error_message is None.
               On failure, costs are 0 and error_message is set.
    """
    total_cost = 0.0
    
    for item_text in items:
        try:
            parts = item_text.split(" - ")[1].split(" x ")
            watts_str = parts[0].replace("W", "").strip()
            usage_hr_str = parts[1].split("hr")[0].strip()
            rate_str = parts[1].split("@ ")[1].replace("₱/kWh", "").strip()

            watts = float(watts_str)
            usage_hr = float(usage_hr_str)
            rate = float(rate_str)
            
            kwh = (watts / 1000) * usage_hr
            cost = kwh * rate
            total_cost += cost
            
        except (ValueError, IndexError, TypeError) as e:
            error_msg = f"Failed to parse item: {item_text}\nError: {e}"
            return 0.0, 0.0, error_msg
            
    monthly_cost = total_cost * 30
    return total_cost, monthly_cost, None


def save_history(user_name, calculation_date, items, daily_cost, monthly_cost):
    """
    Saves the calculation results to a user-specific history file.
    
    Args:
        user_name (str): The name of the current user.
        calculation_date (str): The date of the calculation (e.g., "2025-11-12").
        items (list[str]): A list of strings for each appliance.
        daily_cost (float): The total daily cost.
        monthly_cost (float): The total monthly cost.
    """
    if not user_name:
        return # Don't save if there's no user

    try:
        user_dir = os.path.join(os.getcwd(), "users", user_name)
        os.makedirs(user_dir, exist_ok=True)
        history_path = os.path.join(user_dir, "history.txt")
        
        with open(history_path, "a", encoding="utf-8") as f:
            f.write(f"---- New Calculation ({calculation_date}) ----\n")
            
            for item in items:
                f.write(item + "\n")
                
            f.write(f"Total Daily: ₱{daily_cost:.2f}, Monthly: ₱{monthly_cost:.2f}\n\n")
            
    except OSError as e:
        # Error logging
        print(f"Error saving history: {e}")