rate=0

def square(price):
    a = int(input("Enter side a: "))
    s = a ** 2
    total_price = s * price + broker(s * price)
    print(f"Total price is: {total_price:.3f} $")


def rectangle(price):
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    s = a * b
    total_price = s * price + broker(s * price)
    print(f"Total price is: {total_price:.3f} $")


def triangle(price):
    print("Please enter three sides: a, b, c")
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    total_price = s * price + broker(s * price)
    print(f"Total price is: {total_price:.3f} $")


def circle(price):
    r = int(input("Enter radius r: "))
    s = (r ** 2) * 3.14
    total_price = s * price + broker(s * price)
    print(f"Total price is: {total_price:.3f} $")


def broker(amount):
    return amount * (rate / 100)


def menu():
    print("\nWelcome to Geometry Price Calculator!")
    print("-" * 50)
    print("1: Square")
    print("2: Rectangle")
    print("3: Triangle")
    print("4: Circle")
    print("5: Exit")
    print("-" * 50)
    sel = int(input("Please select an option (1-5): "))
    return sel


while True:
    sel = menu()
    if sel == 5:
        print("Goodbye!")
        break

    price = float(input("Enter price: "))
    rate = float(input("Enter broker commission(%): "))

    if sel == 1:
        square(price)
    elif sel == 2:
        rectangle(price)
    elif sel == 3:
        triangle(price)
    elif sel == 4:
        circle(price)
    else:
        print("Invalid selection.")