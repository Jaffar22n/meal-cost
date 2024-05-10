def calculate_meal_cost():
    while True:
        try:
            food_charge = float(input("Enter the charge for the food: "))
            if food_charge <= 0:
                raise ValueError("Food charge must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    
    tip = food_charge * 0.18
    sales_tax = food_charge * 0.07
    total_price = food_charge + tip + sales_tax
    
    print(f"Food Charge: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales Tax (7%): ${sales_tax:.2f}")
    print(f"Total Price: ${total_price:.2f}")

calculate_meal_cost()
