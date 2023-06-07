#Making a simple class

class car:    #my class name is car

    pass      #here I am using pass statement

obj1=car()      #Here obj1 is an object of class 'car'

#Now we we will add some attributes that will belongs to our class 'car' or object of class 'obj'

class my_car:
    def __init__(self, name, model, year) -> None:   # here I am using a constructor __init__. which is a special type of function which is 
                                                    #only initialize when the object is creates. It is taking three arg i.e name, model, year and self which is a object.
        self.name=name
        self.model=model
        self.year=year

obj2=my_car("Audi","A4", "2022")
print(obj2.model)
print(obj2.name)
print(obj2.year)


#We can also add some methods in this class. Let's see the examples.

# class my_car:
#     def __init__(self, name, model, year) -> None:   # here I am using a constructor __init__. which is a special type of function which is 
#                                                     #only initialize when the object is creates. It is taking three arg i.e name, model, year and self which is a object.
#         self.name=name
#         self.model=model
#         self.year=year
        
#     def owner(self,owner_name):  #we can also call the class method by class's object.
#         return f"the owner of this car is:  {owner_name}"
    
#     def expiry_date(self, date):   #we have another method 'expiry_date in the class 'my_car'.
#         return f"The expiry date of this car is:  {date}"

# obj2=my_car("Audi","A4", "2022")
# print(obj2.model)
# print(obj2.name)
# print(obj2.year)
# print(obj2.owner("sonu"))  #We have called owner method using objj.owner
# print(obj2.expiry_date("21-05-2050"))


#let's move to the @staticmethod.
class my_car:
    price='$2.4M'
    def __init__(self, name, model, year, price) -> None:   # here I am using a constructor __init__. which is a special type of function which is 
                                                    #only initialize when the object is creates. It is taking three arg i.e name, model, year and self which is a object.
        self.name=name
        self.model=model
        self.year=year
        self.price=price
        
    def owner(self,owner_name):  #we can also call the class method by class's object.
        return f"the owner of this car is:  {owner_name}"
    
    def expiry_date(self, date):   #we have another method 'expiry_date in the class 'my_car'.
        return f"The expiry date of this car is:  {date}"
    
    @staticmethod 
    def check_engine():
        print (f"Yes, the engine is working")
    #to print is cng available
    def check_cng():
        print  (f"Yes, cng is available. Its a budget car.")


    @classmethod
    def get_my_car_info(cls):
        print(f"The car is first class working and car's price is {cls.price}")
#Now we can call the def check_engine and def check_eng with the class only. we don't need to make the object to call it.


obj2=my_car("Audi","A4", "2022", "$2.4M")

print(obj2.model)
print(obj2.name)
print(obj2.year)
print(obj2.price)
print(obj2.owner("sonu"))  #We have called owner method using objj.owner
print(obj2.expiry_date("21-05-2050"))
my_car.check_cng()
my_car.check_engine()
my_car.get_my_car_info()


#Let's move to the classmethod now.




