#declare the class for your hotel details
import datetime
class MyHotel:
    def __init__(self, total_bill = '', total_rent= 0, food_bill = 0, addition_charges = 1000, name = '', email = '', contact = '', indate = '', outdate = '', rno = 1):
        print("\n\n\n***********WELCOME TO HOTEL DALAS!!!!!***************\n\n")
        self.total_bill = total_bill
        self.total_rent = total_rent #total rent
        self.food_bill = food_bill
        self.addition_charges = addition_charges
        self.name = name
        self.email = email
        self.contact = contact
        self.indate = datetime.datetime.now()
        self.outdate = outdate
        self.rno = rno
    #customer information
    def customer_info(self):
        self.name = str(input("\nEnter your fullname: "))
        self.email = str(input("Enter your email_address: "))
        self.contact = input("Enter your contact info: ")
        self.indate = print(f"Your indate and time is: {datetime.datetime.now()}")
        self.outdate = input("Please enter the date you'd like to leave: ")
        print("Your room number: ", self.rno,"\n\n")
    #room rent
    def roomrent(self):
        print("\n\nPlease choose a room according to the class you prefer:--")
        print("1.CLASSA ------------> 4000")
        print("2.CLASSB ------------> 3000")
        print("3.CLASSC ------------> 2000")
        print("4.CLASSD ------------> 1000")
        customer_choice = int(input("Entter the number you have choosen: "))
        nights = int(input("How many nights will you spend at the hotel: "))
        if (customer_choice == 1):
            print("You have a room in CLASSA")
            self.total_rent = 4000*nights
        elif (customer_choice == 2):
            print("You have a room in CLASSB")
            self.total_rent = 3000*nights
        elif (customer_choice == 3):
            print("You have a room in CLASSC")
            self.total_rent = 2000*nights
        elif (customer_choice == 4):
            print("You have a room in CLASSD")
            self.total_rent = 1000*nights
        else:
            print("please choose a room")
        print("Your total roomrent is:--------> ", self.total_rent, "\n")
    #food purchase
    def foodpurchased(self):

 
        print("\n\n*****RESTAURANT MENU*****\n\n")
 
        print("1.Dessert----->100","2.Drinks----->50","3.Breakfast--->90","4.Lunch---->110","5.Dinner--->150","6.Exit", "\n\n")
 
 
        while (1):
                #c stands for the customer food choice
            c=int(input("Enter the number of your choice:"))
 
            if (c==1):

                d=int(input("Enter the quantity:"))
                self.food_bill=self.food_bill+100*d
 
            elif (c==2):

                 d=int(input("Enter the quantity:"))
                 self.food_bill=self.food_bill+50*d
 
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.food_bill=self.food_bill+90*d
 
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.food_bill=self.food_bill+110*d
 
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.food_bill=self.food_bill+150*d
 
            elif (c==6):
                break
            else:
                print("You've Enter an Invalid Key")
        print ("Total food Cost= Ksh---->",self.food_bill,"\n")
    #total bill
    def display(self):
        print ("\n\n******HOTEL BILL******\n\n")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.email)
        print("Customer contacts:", self.contact)
        print ("Check in date:",self.indate)
        print ("Check out date",self.outdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.total_rent)
        print ("Your Food bill is:",self.food_bill)
# calculates total bill the total bill
        self.total_bill =self.total_rent + self.food_bill

        print ("Your sub total Purchased is:",self.total_bill)
        print ("Additional Service Charges is",self.addition_charges)
        print ("Your grandtotal Purchased is:",self.total_bill+self.addition_charges,"\n\n")
        self.rno+=1
#main module that controls the others
def main():
    hotel = MyHotel()
    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Show total cost")

        print("5.EXIT")

        b=int(input("\nEnter the number of your choice:"))

        if (b==1):
            hotel.customer_info()
        if (b==2):
            hotel.roomrent()
        if (b==3):
            hotel.foodpurchased()
        if (b==4):
            hotel.display()
        if (b==5):
            quit()
main()


