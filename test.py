# Modularizing the code into seprate files to test 

from  store import Store
from products import Product


# Footlocker = Store("footlocker")
# Jordan = Product("Air Jordans", 200.00, "shoes")
# Airmax = Product("Airmax", 22.00, "shoes")
# new_balance = Product("ss28", 50.00, "shoes")


Footlocker.add_product(Jordan).add_product(Airmax).add_product(new_balance)

# Jordan.update_price(0.4, is_increased=True)
# print(Jordan.price)
# Footlocker.showproducts()
# Footlocker.inflation(.05, "shoes")
# Footlocker.showproducts()
# Footlocker.set_clearance(.02,"shoes")
# Footlocker.showproducts()

# Jordan.print_info()









