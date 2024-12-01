# Q 1

def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount and subtract it from the original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price
    
# Q 2

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price (or the original price if no discount is applied)
print(f"The final price is: {final_price:.2f}")

