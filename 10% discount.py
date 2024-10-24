# 10% discount for anything above $50 

total_bill = float(input("Enter the total bill: "))

if total_bill > 50:
    discount = total_bill * 0.1
    final_bill = total_bill - discount
    print(f"Discount Applied! Your Final is ${final_bill}.")
else:
    print(f"No discount applied. Your Total bill is ${total_bill}.")

# Movie ticket price

age = int(input("Enter your age: "))

if age <= 12:
    print("Ticket price: $5")
elif age <=17:
    print("Ticket price: $7")
elif age <=64:
    print("Ticket price: $10")
else:
    print("Ticket price: $6")

# Bank Withdrawal(Nested if Else)

