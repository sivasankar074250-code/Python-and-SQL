# Q1
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print(f"Kelvin: {kelvin:.2f} K")

print("\nConversion Table")
print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")

for c in range(-40, 101, 10):
    f = (c * 9 / 5) + 32
    k = c + 273.15
    print(f"{c:10.2f} {f:12.2f} {k:10.2f}")


# Q2
a, b, c = map(float, input("Enter three numbers: ").split())

largest = max(a, b, c)
smallest = min(a, b, c)
average = (a + b + c) / 3

print(f"Largest: {largest:g}")
print(f"Smallest: {smallest:g}")
print(f"Average: {average:.2f}")

n = int(input("Enter a number for classification: "))

if n > 0:
    if n % 2 == 0:
        print("Classification: Positive and Even")
    else:
        print("Classification: Positive and Odd")
elif n < 0:
    if n % 2 == 0:
        print("Classification: Negative and Even")
    else:
        print("Classification: Negative and Odd")
else:
    print("Classification: Zero")


# Q3
year = int(input("Year: "))
marks = float(input("Marks: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 50:
    print("Grade: B")
else:
    print("Grade: Fail")


# Q4
items = []

while True:
    value = input("Enter item price or 'done': ")

    if value.lower() == "done":
        break

    price = float(value)
    items.append(price)

print("\nItem        Price")
print("---------------------")

for i, price in enumerate(items, start=1):
    print(f"Item {i:<5} {price:8.2f}")

print("---------------------")

subtotal = sum(items)

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

amount_after_discount = subtotal - discount
tax = amount_after_discount * 0.18
final_amount = amount_after_discount + tax

print(f"Subtotal    {subtotal:8.2f}")
print(f"Discount    {discount:8.2f}")
print(f"Tax         {tax:8.2f}")
print(f"Final       {final_amount:8.2f}")


# Q5
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Before Swap: a = {a}, b = {b}")

a, b = b, a

print(f"After Swap: a = {a}, b = {b}")


# Q6
principal = float(input("Principal: "))
rate = float(input("Rate: "))
time = float(input("Time: "))

if principal < 0 or time < 0:
    print("Invalid input. Principal and time must be non-negative.")
else:
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"Principal      : {principal:.2f}")
    print(f"Rate           : {rate:.2f}%")
    print(f"Time           : {time:.2f} years")
    print(f"Simple Interest: {simple_interest:.2f}")
    print(f"Total Amount   : {total_amount:.2f}")


# Q7
value = input("Enter a value: ")

print("Original value type :", type(value).__name__)

try:
    integer_value = int(value)
    print("Integer value :", integer_value)
    print("Integer type :", type(integer_value).__name__)
except ValueError:
    print("Invalid integer conversion")

try:
    float_value = float(value)
    print("Float value :", float_value)
    print("Float type :", type(float_value).__name__)
except ValueError:
    print("Invalid float conversion")


# Q8
a = float(input())
b = float(input())

total = a + b

print(f"Sum: {total:.2f}")


# Q9
a, b, c, d, e = 10, 3.14, "Python", True, None

print(f"Value: {a} Type: {type(a).__name__}")
print(f"Value: {b} Type: {type(b).__name__}")
print(f"Value: {c} Type: {type(c).__name__}")
print(f"Value: {d} Type: {type(d).__name__}")
print(f"Value: {e} Type: {type(e).__name__}")


# Q10
a = 19
b = 4

print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print("Negative floor division example")
print("-19 // 4 =", -19 // 4)
