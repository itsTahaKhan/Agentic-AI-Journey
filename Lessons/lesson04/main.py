def classify_passenger(age):
    passenger_classification = 'none'
    if age <= 2:
        passenger_classification = "Infant"
    elif 2 < age <= 12:
        passenger_classification = 'Child'
    else:
        passenger_classification = 'Adult'
    return passenger_classification

def check_baggage(bag_weight):
    if bag_weight <= 23:
        return "Under allowed weight"
    elif 23 < bag_weight <= 32:
        return "Over allowed limit, extra fee required"
    else:
        return "Over weight limit(32KGs)"

def login(input_username, input_password):
    username = "Taha"
    password = 'taha0226'
    return input_username == username and input_password == password
    
while True:
    input_username = str(input("Enter your username: "))
    input_password = str(input("Enter your password: "))
    logged_in = login(input_username,input_password)
    if not logged_in:
        print("Login Failed!")
    if logged_in:
        print("Login Successfull!")
        age = int(input("Enter your age: "))
        print(f"You are classified as: {classify_passengers(age)}")
        bag_weight = float(input("Enter your bag weight(KGs): "))
        print(f"Your baggage is: {check_baggage(bag_weight)}")
        break
