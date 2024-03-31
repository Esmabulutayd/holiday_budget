while True:
    print("Welcome to holiday budget calculator!\n")

    cities = ["Istanbul", "London", "Amsterdam"]

    city_flight = input("Please input the city name you'd like to travel (options: Istanbul, London, Amsterdam): \n").capitalize()

    while city_flight not in cities:
        print("Please choose a city from the list.")
        city_flight = input("Please input the city name you'd like to travel (options: Istanbul, London, Amsterdam): \n").capitalize()

    num_nights = input("Please enter number of the nights you would like to stay: \n")

    while not num_nights.isnumeric():
        print("Please enter a number.")
        num_nights = input("Please enter number of the nights you would like to stay: \n")

    num_nights = int(num_nights)

    rental_days = input("Please enter number of the days you would like to rent a car: \n")

    while not rental_days.isnumeric():
        print("Please enter a number.")
        rental_days = input("Please enter number of the days you would like to rent a car: \n")

    rental_days = int(rental_days)

    def plane_cost(city_flight):
        if city_flight == "Istanbul":
            return 300  # Program assumes cost of Istanbul flight is £300
        elif city_flight == "London":
            return 500  # Program assumes cost of London flight is £500
        elif city_flight == "Amsterdam":
            return 400  # Program assumes cost of Amsterdam flight is £400
        else:
            return 0

    def hotel_cost(num_nights):
        if city_flight == "Istanbul":
            return num_nights * 100  # Program assumes daily hotel rate is £100 in Istanbul
        elif city_flight == "London":
            return num_nights * 250  # Program assumes daily hotel rate is £250 in London
        elif city_flight == "Amsterdam":
            return num_nights * 200  # Program assumes daily hotel rate is £200 in Amsterdam
        else:
            return 0

    def car_rental(rental_days):
        return rental_days * 75  # Program assumes a daily rental cost of £75 for the car

    def holiday_cost(hotel_total, plane_total, car_total):
        return hotel_total + plane_total + car_total

    hotel_total = hotel_cost(num_nights)
    flight_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)

    print(f"Your total holiday cost is: £ {holiday_cost(hotel_total, flight_total, car_total)}")

    choice = input("Would you like to calculate another holiday budget? (yes/no): ").lower()
    if choice != "yes":
        break
