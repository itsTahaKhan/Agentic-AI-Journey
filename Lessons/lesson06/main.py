# my_favorite_programming_languages = [
#     "Python",
#     "JavaScript",
#     "PHP",
#     "Java",
#     "C++"
# ]
# print(my_favorite_programming_languages[0])
# print(my_favorite_programming_languages[-1])
# print(len(my_favorite_programming_languages))

# cities = [
#     "karachi",
#     "lahore",
#     "dubai",
#     "riyadh",
#     "dubai",
#     "hyderabad",
#     "sukkur",
#     "tando adam",
#     "larkana",
#     "london"
# ]

# for index, city in enumerate(cities, start=1):
#     print(f"{index}: {city}")

HOTELS = [
            "Hotel 1: PC Karachi, 20SAR Per Night",
            "Hotel 2: PC Riyadh, 18SAR Per Night",
            "Hotel 3: PC Lahore, 35SAR Per Night",
            "Hotel 4: PC Medina, 25SAR Per Night"
        ]

FLIGHTS = [
            "RUH TO MED | 320SAR",
            "RUH TO JED | 420SAR",
            "RUH TO KHI | 800SAR",
            "RUH TO LHR | 680SAR"
        ]

def show_flights():
    while True:
        
        for index, flight in enumerate(FLIGHTS, start=1):
            print(f"{index}: {flight}")
        choice = int(input("Enter the flight number to book: "))
        if(len(FLIGHTS) >= choice >= 1):
            return FLIGHTS[choice - 1]
        else:
            print("Choose Correct option")

def show_hotels():
    while True:
        for index, hotel in enumerate(HOTELS, start=1):
            print(f"{index}: {hotel}")
        choice = int(input("Enter hotel number you want to book: "))
        if(len(HOTELS) >= choice >= 1):
            return HOTELS[choice - 1]
        else:
            print("Choose correct option")

def show_bookings(booked_flights, booked_hotels):
    if(booked_flights):
        print("Booked Flights: \n")
        for index, flight in enumerate(booked_flights, start=1):
            print(f"{index}: {flight}")
    else:
        print("No flights booked!")
    if(booked_hotels):
        print("Booked Hotels: \n")
        for index, hotel in enumerate(booked_hotels, start=1):
            print(f"{index}: {hotel}")
    else:
        print("No hotels booked")
    
def show_menu():
    booked_flights, booked_hotels = [], []
    while True:
        print("\n====== Airline Reservation System ======\n")
        print("1. Search Flights")
        print("2. Book Hotel")
        print("3. View Booking")
        print("4. Logout")
        choice = int(input("Choose one: "))
        if(choice == 1):
            print("\n\nSearching Flights...\n")
            booked_flights.append(show_flights())
        elif(choice == 2):
            print("\n\nSearching Hotels...\n")
            booked_hotels.append(show_hotels())
        elif(choice == 3):
            print("\n\nLoading Details...\n")
            show_bookings(booked_flights, booked_hotels)
        else:
            print("Logged Out!\n")
            break


show_menu()