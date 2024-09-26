from computer import * 
from typing import Optional

#Setting ResaleShop class
class ResaleShop:

    # Attribuite
    inventory: list

    # Constructor
    def __init__(self):
        self.inventory = []
    
    # Adding bought computer in the inventory
    def buy(self, buying_computer):
        if buying_computer in self.inventory:
            print("we already purchased this computer before")
        else: 
            self.inventory.append(buying_computer)
            print("Yay, we bought this computer")

    # Removing sold computer in the inventory
    def sell(self, selling_computer):
        if selling_computer in self.inventory:
            self.inventory.remove(selling_computer)
            print("Yay, we sold this computer")
        else: 
            print("we do not have this computer")

    # Updating the price 
    def update_price(self, updating_computer, new_price: int):
        if updating_computer in self.inventory:
            updating_computer.price = new_price
            print("price updated to", updating_computer.price)
        else:
            print("this computer is not found. Cannot update price.")

    # Printing all descriptions of objects in the inventory
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for each in self.inventory:
                # Print its details
                print(f'Item #{self.inventory.index(each)} : {each.description}')
        else:
            print("No inventory to display.")

    # Resetting the price based on year-made, and the OS (optional)
    def refurbish(self, refurbishing_computer, new_os: Optional[str] = None):
        if refurbishing_computer in self.inventory:
            if int(refurbishing_computer.year_made) < 2000:
                refurbishing_computer.price = 0 # too old to sell, donation only
            elif int(refurbishing_computer.year_made) < 2012:
                refurbishing_computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(refurbishing_computer.year_made) < 2018:
                refurbishing_computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                refurbishing_computer.price = 1000 # recent stuff
            if new_os is not None:
                refurbishing_computer.operating_system = new_os # update details after installing new OS
            print(f'Successfully refurbished ->\nprice: {refurbishing_computer.price}, system: {refurbishing_computer.operating_system}')
        else:
            print("This computer is not found. Please select another item to refurbish.")
    
def main():
    my_ResaleShop = ResaleShop()
    my_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    my_computer2 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.buy(my_computer2)
    my_ResaleShop.update_price(my_computer, 3000)
    my_ResaleShop.print_inventory()
    my_ResaleShop.refurbish(my_computer, "Mac Pro (2024)")

if __name__ == "__main__": 
    main()