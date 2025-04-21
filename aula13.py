import math

# Using a function to collect data
# Calculating Bhaskara's formula

bhaskara_a = int(input("What's the value of a? "))
bhaskara_b = int(input("What's the value of b? "))
bhaskara_c = int(input("What's the value of c? "))

delta = (bhaskara_b ** 2) - (4 * bhaskara_a * bhaskara_c)
print(f'Delta: {delta}')

if delta < 0:
    print("No real roots exist.")
else:
    bhaskara_x1 = (-bhaskara_b + math.sqrt(delta)) / (2 * bhaskara_a)
    print(f'Bhaskara x1: {bhaskara_x1:,.2f}')

    bhaskara_x2 = (-bhaskara_b - math.sqrt(delta)) / (2 * bhaskara_a)
    print(f'Bhaskara x2: {bhaskara_x2:,.2f}')