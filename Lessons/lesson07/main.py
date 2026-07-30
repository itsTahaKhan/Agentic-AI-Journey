student = {
    "name": "Taha",
    "age": 24,
    "favorite_language": "Python",
    "dream_company": "System LTD"
}

for key, value in student.items():
    print(f"{key}: {value}")

print(student['name'])
print(student['dream_company'])

flight = {
    'origin': 'RUH',
    'destination': 'JED',
    'airline': 'Saudia',
    'price': 420,
    'currency': 'SAR'
}

print(flight['destination'])
flight['price'] = 450
flight['seat'] = '12A'
for key, value in flight.items():
    print(f"{key}: {value}")

HOTELS = [
    {
        "hotel_name": "Pearl Continental",
        "location": "Karachi",
        "beds": "1 King bed",
        "rent": "7000",
        "currency": "PKR"
    },
    {
        "hotel_name": "MERL",
        "location": "Riyadh",
        "beds": "2 Beds",
        "rent": "20",
        "currency": "SAR"
    }
        ]

FLIGHTS = [
    {
        "origin": "RUH",
        "destination": "MED",
        "price": 320,
        "currency": "SAR"
    },
    {
        "origin": "RUH",
        "destination": "JED",
        "price": 420,
        "currency": "SAR"
    }
]

def show_items(item_type, items):
    while True:
        for index, item in enumerate(items, start=1):
            print(f"================================\n{item_type.capitalize()} {index}")
            for key, value in item.items():
                print(f"{key}: {value}")
        choice = int(input(f"Enter the {item_type} number to book: "))
        if(len(items) >= choice >= 1):
            return items[choice - 1]
        else:
            print("Choose Correct option")

def show_hotels():
    while True:
        for index,hotel in enumerate(HOTELS, start=1):
            print(f"================================\nHotel {index}")
            for key, value in hotel.items():
                print(f"{key}: {value}")
        choice = int(input("Enter hotel number you want to book: "))
        if(len(HOTELS) >= choice >= 1):
            return HOTELS[choice - 1]
        else:
            print("Choose correct option")

def show_bookings(booked_flights, booked_hotels):
    if(booked_flights):
        print("Booked Flights:")
        for index, flight in enumerate(booked_flights, start=1):
            print(f"================================\nFlight {index}")
            for key, value in flight.items():
                print(f"{key}: {value}")
            # print(f"{index}: {flight}")
    else:
        print("================================\nNo flights booked!")
    if(booked_hotels):
        print("\nBooked Hotels:")
        for index,hotel in enumerate(booked_hotels, start=1):
            print(f"================================\nHotel {index}")
            for key, value in hotel.items():
                print(f"{key}: {value}")
    else:
        print("================================\nNo hotels booked")
    
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
            booked_flights.append(show_items("flight", FLIGHTS))
        elif(choice == 2):
            print("\n\nSearching Hotels...\n")
            booked_hotels.append(show_items("hotel", HOTELS))
        elif(choice == 3):
            print("\n\nLoading Details...\n")
            show_bookings(booked_flights, booked_hotels)
        else:
            print("Logged Out!\n")
            break


show_menu()