# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.
       Applies discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = (discount_percent / 100) * price
        # Subtract discount from original price
        final_price = price - discount_amount  
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price  

# Get user input for price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount in percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)

