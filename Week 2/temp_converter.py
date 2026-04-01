print("--- Mini Project 3: Temperature Converter ---")
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9

while True:
    print("\n1. Celsius to Fahrenheit   2. Fahrenheit to Celsius   3. Exit")
    choice = input("Choose conversion (1/2/3): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f" {c}°C is equal to {c_to_f(c):.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f" {f}°F is equal to {f_to_c(f):.2f}°C")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")