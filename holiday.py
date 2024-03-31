
# Define necessary functions
# This function calculates flight cost based on the city chosed
def plane_cost(city_flight):

    if city_flight == "Istanbul":
        return 300  # Program assumes cost of Istanbul flight is £300
    elif city_flight == "London":
        return 500  # Program assumes cost of London flight is £500
    elif city_flight == "Amsterdam":
        return 400  # Program assumes cost of Amsterdam flight is £400
    else:
        return 0

# This function calculates hotel cost based on the city chosed
def hotel_cost(num_nights):

    if city_flight == "Istanbul":
        return num_nights * 100  # Program assumes daily hotel rate is £100 in Istanbul
    elif city_flight == "London":
        return num_nights * 250  # Program assumes daily hotel rate is £250 in London
    elif city_flight == "Amsterdam":
        return num_nights * 200  # Program assumes daily hotel rate is £200 in Amsterdam
    else:
        return 0

# This function calculates total car rental cost, assuming daily cost of £75 for the car
def car_rental(rental_days):

    return rental_days * 75  

# This function calculates total holiday cost which is a sum of hotel, flight and car rental costs
def holiday_cost(hotel_total, plane_total, car_total):

    return hotel_total + plane_total + car_total

# Infinite loop to continuously calculate holiday budgets until user chooses to stop
while True:
    # Welcome message
    print("Welcome to holiday budget calculator!\n")

    # List of cities where user can travel
    cities = ["Istanbul", "London", "Amsterdam"]

    # Prompting user to input their desired travel city
    city_flight = input("Please input the city name you'd like to travel (options: Istanbul, London, Amsterdam): \n").capitalize()

    # Validating user input for city selection
    while city_flight not in cities:
        print("Please choose a city from the list.")
        city_flight = input("Please input the city name you'd like to travel (options: Istanbul, London, Amsterdam): \n").capitalize()

    # Prompting user to input number of nights for stay
    num_nights = input("Please enter number of the nights you would like to stay: \n")

    # Validating user input for number of nights
    while not num_nights.isnumeric():
        print("Please enter a number.")
        num_nights = input("Please enter number of the nights you would like to stay: \n")

    # Converting number of nights to integer
    num_nights = int(num_nights)

    # Prompting user to input number of days for car rental
    rental_days = input("Please enter number of the days you would like to rent a car: \n")

    # Validating user input for number of rental days
    while not rental_days.isnumeric():
        print("Please enter a number.")
        rental_days = input("Please enter number of the days you would like to rent a car: \n")

    # Converting number of rental days to integer
    rental_days = int(rental_days)
    
    # Calculating total hotel cost
    hotel_total = hotel_cost(num_nights)
    
    # Calculating total flight cost based on selected city
    flight_total = plane_cost(city_flight)
    
    # Calculating total car rental cost
    car_total = car_rental(rental_days)

    # Calculating and displaying the total holiday cost
    print(f"Your total holiday cost is: £ {holiday_cost(hotel_total, flight_total, car_total)}")

    # Asking user if they want to calculate another holiday budget
    choice = input("Would you like to calculate another holiday budget? (yes/no): ").lower()
    
    # Exiting loop if user does not want to calculate another budget
    if choice != "yes":
        break
