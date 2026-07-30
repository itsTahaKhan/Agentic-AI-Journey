# passenger = {
#     "name": "Taha",
#     "passport": "AB123456",
#     "nationality": "Pakistani",
#     "age": 24
# }

# print(passenger["name"])
# print(passenger["passport"])

bookings = {
        "passenger": {
            "name": "Taha",
            "passport_number": "weqw21312",
            "pass": "0226",
            "dob": "02/11/2001"
        },
        "flight": {
            "flight_number": "DXB231",
            "origin": "Dubai",
            "destination": "Riyadh",
            "ticket_price": 560,
            "currency": "SAR"
        },
        "hotel": {
            "loction": "Karachi",
            "hotel_name": "Pearl Continental",
            "price_per_night": "30",
            "currency": "SAR"
        }
    }

for key, value in bookings:
    for sub_key, sub_value in value:
        print(f"{key}: {value}")