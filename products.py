# Create a Products class with 3 attributes 



class Product :
    def __init__(self,name, price, category) :
        self.name = name 
        self.price = price
        self.category = category


    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price +=  (percent_change *self.price)
        else:
            is_increased == False
            self.price -= (percent_change * self.price)


    def print_info (self):
        print(f'{self.name}, {self.price}, {self.category}')
        


