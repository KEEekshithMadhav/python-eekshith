# python-eekshith
 # Get input from the user
>>> bill_amount = float(input("Enter the total bill amount: $"))
Enter the total bill amount: $2760
>>> tip_percentage = float(input("Enter the tip percentage: "))
Enter the tip percentage: 1.5
>>> # Calculate the tip amount
>>> tip_amount = bill_amount * (tip_percentage / 100)
>>> # Calculate the total bill including tip
>>> total_bill = bill_amount + tip_amount
>>> # Display the results
>>> print(f"\nTip Amount: ${tip_amount:.2f}")

Tip Amount: $41.40
>>> print(f"Total Bill Including Tip: ${total_bill:.2f}")
Total Bill Including Tip: $2801.40
