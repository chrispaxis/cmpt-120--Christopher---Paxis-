from math import prod


class ProductInformation:

    #The following defines the constructor
    def __init__(self, IDnumber, name, price, quantity):
        self.IDnumber = IDnumber
        self.name = name
        self.price = price
        self.quantity = quantity

    #Determines if there is stock available
    def in_stock(self, quantity):
        return self.quantity >= quantity

    #Subtracts the purchased quantity from the old quantity to get new total
    def updated_stock(self, quantity):
        self.quantity -= quantity
  
    #Multiples the price by quantity of product purchased to get price
    def prod_cost(self):
        return self.price * self.quantity


prod1 = ProductInformation(0, "Ultrasonic range finder", 2.50, 4)
prod2 = ProductInformation(1, "Serveo Motor", 14.99, 10)
prod3 = ProductInformation(2, "Servo Controller", 44.95, 5)
prod4 = ProductInformation(3, "Microcontroller Board", 34.95, 7)
prod5 = ProductInformation(4, "Laser range finder", 149.99, 2)
prod6 = ProductInformation(5, "Lithium polymer battery", 8.99, 8) 

products = [prod1, prod2, prod3, prod4, prod5, prod6]

#Lists the product information
def print_stock():
    print("\nAvailable Products")
    print("-------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(f"{str(i)}) {products[i].name}, ${products[i].price}, {products[i].quantity} left in stock")
    print()


    #Input cash amount
    #Enter product ID and amount of that product you want 
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter product ID and quantity you wish to buy. Separate the values with with a comma: ").split(",")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])


        product = None
        for i in products:
            if i.IDnumber == prod_id:
                product = i
        
        #Only procuts with valid ID are found
        if product == None:
            print(f"Product with ID {prod_id} not found.")
            continue


        #Ran out of stock notice
        if not product.in_stock(count):
            print("Not enough quantity!")
            continue
        
        #Calculates price of product * quantity
        price = product.price * count

        #Insufficient funds notice
        if cash < price:
            print("Sorry, you cannot afford that!")
        
        #Updates the stock quantity after purchase
        #Subtracts the price from the cash remaining
        product.updated_stock(count)
        cash -= price

        print("You have $", "{0:.2f}".format(cash), "remaining.")

        
main()