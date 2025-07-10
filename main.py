class Cab:
    #Initialize cab details

    def __init__(self, cab_id, driver_name, rate_per_km):
        self.cab_id = cab_id
        self.driver_name = driver_name
        self.rate_per_km = rate_per_km
        self.is_available = True

    # Show Cab info
    def show_info(self):

        status = "Available" if self.is_available else "Booked"

        print(f"Cab ID: {self.cab_id}, Driver : {self.driver_name}, Rate : Rs.{self.rate_per_km}, Status : {status}")


class Booking:
    # Initialize booking manager with Cab

    def __init__(self):
        self.cabs = [
            Cab(1, "Murthy", 15),
            Cab(2, "Karthik", 18),
            Cab(3, "Kvel", 19),
        ]

    def show_all_cab(self):
        print("\n Available Cabs")
        for cab in self.cabs:
            cab.show_info()

    def book_cab(self):
        cab_id = int(input("Enter the Cab ID to book : "))
        distance = float(input("Enter the distance(km) : "))

        for cab in self.cabs:
            if cab.cab_id == cab_id:
                if cab.is_available:
                    fare = distance * cab.rate_per_km
                    cab.is_available = False

                    print(f"Cab Booked ! Fare : Rs.{fare}")

                else:

                    print("Cab is already booked.")

                return


        print("Invalid Cab ID")

    def cancel_booking(self):

        cab_id = int(input("Enter Cab ID to cancel the Booking : "))

        for cab in self.cabs:
            if cab.cab_id == cab_id:
                if not cab.is_available:
                    cab.is_available = True
                    print("Booking Cancelled.")

                else:
                    print("Cab is not Booked.")

                return

        print("Invalid Cab ID")

def main():
    booking = Booking()

    while True:
        print("\n ---Cab Booking Menu")
        print("1. Show all Cabs")
        print("2. Book a Cab")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            booking.show_all_cab()

        elif choice == 2:
            booking.book_cab()

        elif choice == 3:
            booking.cancel_booking()

        elif choice == 4:
            print("Thank you for using Cab Booking App")
            break

        else:
            print("Invalid Choice")


# Entry Point of app

if __name__ == "__main__":
    main()

