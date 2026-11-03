def mealDiscount():
    try:
        # 1. Asks for meal bill
        bill = float(input("Enter the total meal bill: "))
        
        # 2. Asks if Student or Non student
        status = input("Are you a (S)tudent or (N)on student? ").lower()

        discount_rate = 0.0
        
        # 3. Applies 15 percent or 5 percent discount
        if status == 's':
            discount_rate = 0.15 # 15%
        elif status == 'n':
            discount_rate = 0.05 # 5%
        else:
            print("Invalid status entered. Applying 5% Non-student discount.")
            discount_rate = 0.05

        discount_amount = bill * discount_rate
        final_payment = bill - discount_amount

        # 4. Displays final payment
        print(f"\nOriginal Bill: ${bill:.2f}")
        print(f"Discount Rate: {discount_rate * 100:.0f}%")
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Final Payment: ${final_payment:.2f}")

    except ValueError:
        print("Error: Bill amount must be a numeric value.")

# Show how to call the function
mealDiscount()