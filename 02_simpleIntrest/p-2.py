def calculate_simple_interest(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    return simple_interest
principal = float(input("Enter the principal amount (P): "))
time = float(input("Enter the time period in years (T): "))
rate = float(input("Enter the annual interest rate (R): "))
interest = calculate_simple_interest(principal, time, rate)
print(f"Principal amount (P): {principal}")
print(f"Time period in years (T): {time}")
print(f"Annual interest rate (R): {rate}")
print(f"Simple Interest: {interest}")