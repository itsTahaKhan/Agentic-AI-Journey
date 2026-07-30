def calcuate_tax(base_price, tax):
    tax = base_price * tax / 100
    return tax

def can_book_flight(age):
    if(age<18):
        eligible = False
    else:
        eligible = True
    return eligible

base_price = float(input("Enter ticket price($USD): "))
tax = float(input("Enter tax percentage($USD): "))

ticket_price = base_price + calcuate_tax(base_price, tax)
print(ticket_price)

age = int(input("Enter your age: "))
eligible = can_book_flight(age)
print(eligible)
if (eligible):
    print("You are eligible to book a flight")
    
else:
    print("You are not eligible to book a flight")