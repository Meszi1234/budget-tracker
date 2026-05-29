# Ask the user to type an amount (e.g. 50.00 for income, -12.50 for an expense)
amount_input = input("Enter amount (positive for income, negative for expense): ")

# Convert the text the user typed into a decimal number so we can work with it
amount = float(amount_input)

# Ask the user for a short description of the transaction
description = input("Enter description: ")

# Print a blank line to separate input from output
print()

# Show the transaction back to the user to confirm it was recorded correctly
print("Transaction recorded:")
print(f"  Description: {description}")
print(f"  Amount:      ${amount:.2f}")  # :.2f formats the number to always show 2 decimal places
