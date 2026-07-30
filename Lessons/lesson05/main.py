# x = 1
# while x <= 20:
#     print(x)
#     x+=1

# for x in range(1,21):
#     print(x)

# built_in_pass = "OpenAI2026"
# while True:
#     password = str(input("Enter password: "))
#     if(password == built_in_pass):
#         print("Welcome!")
#         break

def show_flights():
    while True:
        print("Flight 1: RUH TO MED, 320SAR")
        print("Flight 2: RUH TO JED, 420SAR")
        print("Flight 3: RUH TO KHI, 800SAR")
        print("Flight 4: RUH TO LHR, 680SAR")
        choice = int(input("Enter the flight number to book: "))
        if(choice == 1):
            flight = "RUH TO MED, 320SAR"
            break
        elif(choice == 2):
            flight = "RUH TO JED, 420SAR"
            break
        elif(choice == 3):
            flight = "RUH TO KHI, 800SAR"
            break
        elif(choice == 4):
            flight = "RUH TO LHR, 680SAR"
            break
        else:
            print("Choose Correct option")
    return flight

def show_hotels():
    while True:
        print("Hotel 1: PC Karachi, 20SAR Per Night")
        print("Hotel 2: PC Riyadh, 18SAR Per Night")
        print("Hotel 3: PC Lahore, 35SAR Per Night")
        print("Hotel 4: PC Medina, 25SAR Per Night")
        choice = int(input("Enter hotel number you want to book: "))
        if(choice == 1):
            hotel = "PC Karachi"
            break
        elif(choice == 2):
            hotel = "PC Riyadh"
            break
        elif(choice == 3):
            hotel = "PC Lahore"
            break
        elif(choice == 4):
            hotel = "PC Medina"
            break
        else:
            print("Choose correct option")
    return hotel

def show_bookings(flight, hotel):
    if(flight):
        print("Booked Flight: \n", flight )
    else:
        print("No flights booked!")
    if(hotel):
        print("Booked Hotel: \n", hotel)
    else:
        print("No hotels booked")
    
def show_menu():
    flight, hotel = '', ''
    while True:
        print("\n====== Airline Reservation System ======\n")
        print("1. Search Flights")
        print("2. Book Hotel")
        print("3. View Booking")
        print("4. Logout")
        choice = int(input("Choose one: "))
        if(choice == 1):
            print("\n\nSearching Flights...\n")
            flight = show_flights()
            print(flight)
        elif(choice == 2):
            print("\n\nSearching Hotels...\n")
            hotel = show_hotels()
        elif(choice == 3):
            print("\n\nLoading Details...\n")
            show_bookings(flight, hotel)
        else:
            print("Logged Out!\n")
            break


show_menu()