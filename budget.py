import csv  # provides csv.writer for writing rows to a CSV file
import os   # provides os.path.isfile to check if the CSV already exists

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

# Path to the CSV file that stores all transactions
csv_file = "transactions.csv"

# Check whether the file exists before opening it, so we know if a header is needed
file_exists = os.path.isfile(csv_file)

# Open in append mode ("a") so previous transactions are never overwritten
# newline="" is required by the csv module to prevent extra blank lines on Windows
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)  # create a writer that formats rows as comma-separated values

    # Write the header only when creating the file for the first time
    if not file_exists:
        writer.writerow(["amount", "description"])

    # Write this transaction as a new row: amount first, then description
    writer.writerow([amount, description])
