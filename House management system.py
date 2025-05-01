# House Management System

class House:
    def __init__(self, house_id, owner_name, address, rent):
        self.house_id = house_id
        self.owner_name = owner_name
        self.address = address
        self.rent = rent

    def display_details(self):
        print(f"House ID: {self.house_id}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Address: {self.address}")
        print(f"Rent: ${self.rent}")


class HouseManagementSystem:
    def __init__(self):
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)
        print("House added successfully!")

    def remove_house(self, house_id):
        for house in self.houses:
            if house.house_id == house_id:
                self.houses.remove(house)
                print("House removed successfully!")
                return
        print("House not found!")

    def list_houses(self):
        if not self.houses:
            print("No houses available.")
        else:
            for house in self.houses:
                house.display_details()
                print("-" * 20)


# Example usage
if __name__ == "__main__":
    system = HouseManagementSystem()

    while True:
        print("\nHouse Management System")
        print("1. Add House")
        print("2. Remove House")
        print("3. List Houses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            house_id = input("Enter House ID: ")
            owner_name = input("Enter Owner Name: ")
            address = input("Enter Address: ")
            rent = float(input("Enter Rent: "))
            house = House(house_id, owner_name, address, rent)
            system.add_house(house)
        elif choice == "2":
            house_id = input("Enter House ID to remove: ")
            system.remove_house(house_id)
        elif choice == "3":
            system.list_houses()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")