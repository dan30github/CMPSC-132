#Lab #5
#Due Date: 09/21/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: I did not ask for help       
#
########################################
class SodaMachine:
    '''
        Creates instances of the class SodaMachine. Takes a string and an integer

        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    #-- start code here ---
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0
    #-- ends here ---

    def purchase(self):
    #-- start code here ---
        if self.stock == 0:
            return 'Product out of stock'
        else:
            if self.balance < self.price:
                return 'Please deposit $'+ str(self.price - self.balance)
            elif self.balance == self.price:
                self.stock -= 1
                self.balance = 0
                return 'Coke dispensed'
            elif self.balance > self.price:
                self.stock -= 1
                old_balance = self.balance
                self.balance = 0
                return 'Coke dispensed, take your $'+str(old_balance-self.price)
                


    #-- ends here ---

    def deposit(self, amount):
    #-- start code here ---
        if self.stock >= 1:
            self.balance += amount
            return 'Balance: $' + str(self.balance)
        else:
            return 'Sorry, out of stock. Take your $'+str(amount) + ' back'

    #-- ends here ---

    def restock(self, amount):
    #-- start code here ---
        self.stock += amount
        return 'Current soda stock: ' + str(self.stock)

    #-- ends here ---
    

class Line:
    ''' 
       Creates objects of the class Line, takes 2 tuples
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''


    def __init__(self, coord1, coord2):
    #-- start code here ---
        self.x1 = coord1[0]
        self.y1 = coord1[1]

        self.x2 = coord2[0]
        self.y2 = coord2[1]


    #-- ends here ---
    
    #PROPERTY METHODS
    @property
    def distance(self):
    #-- start code here ---
        return round(math.sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2)), 3)

        round( ( ((self.x2 - self.x1)**2 + (self.y2 - self.y1**2))**(1/2)) , 3)


    #-- ends here ---
    @property
    def slope(self):
    #-- start code here ---
        if (self.x2 - self.x1) == 0:
            return 'Infinity'
        else:
            return((self.y2 - self.y1) / (self.x2 - self.x1))

    #-- ends here ---
