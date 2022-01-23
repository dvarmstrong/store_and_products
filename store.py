#  Create a store Class that has two attributes a name and a list of products




from products import Product


class Store :
    def __init__(self, name):
        self.name = name 
        self.products =  []

# Add a product to the store 
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

# Removes the products from the store list of Products and prints its info
    def sell_product(self, id):
        id == self.products[0:] 
        self.products.pop(id)
        print(self.products)
        return self

# Increases the price of each product by the percent _increase given from the products class
    def inflation(self, percent_increase, category):
        if self.products:
            for product in self.products:
                if product.category == category:
                    product.price = percent_increase * product.price + product.price
        return self 
    
    
# updates all the products matching the given category by reducing the price by the percent_discount given from the product class   
    def set_clearance(self, percent_discount,category,):
        if self.products:
            for product in self.products:
                if product.category == category:
                    product.price = product.price - (product.price * percent_discount) 
        return self

    


    def showproducts(self):
        # self.products = Product.print_info()
        # print(f"{self.name}, {self.products}")
        if self.products:
            for product in self.products:
                product.print_info()




