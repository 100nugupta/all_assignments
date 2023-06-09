from abc import ABC,abstractclassmethod
class SHOPKEEPER_NAME(ABC):
     @abstractclassmethod
     def owner_name(self, owner_names):
       return f"the owner is {owner_names}"
     
class ADDRESS:
    @abstractclassmethod
    def get_address(self, address):
        return f"the address of the shop is {address}"
        
        



class SHOP(SHOPKEEPER_NAME, ADDRESS):
    def __init__(self, shopkeeper_name):
        self.shopkeeper_name= shopkeeper_name
    
    def shop_number(self, shop_no):
        return f"shop number is {shop_no}"
    def owner_name(self, owner_names):
        return f"the owner is {owner_names}"
    def get_address(self, address):
        return f"the address of the shop is {address}"


class BILL(SHOPKEEPER_NAME, ADDRESS):
    def __init__(self, bill_number):
        self.bill_number=bill_number

    def shop_number(self, shop_no):
        return f"{shop_no}"
    
    def owner_name1(self, owner_names):
        return f"the owner is {owner_names}"
    
    def get_address(self, address):
        return f"the address of the shop is {address}"
    

# obj1=SHOP("pujari")
# print(obj1.shop_number(12))


obj2=SHOP("Raghav")
print(obj2.owner_name('ragahv'))



# obj3=BILL(122)
# print(obj3.bill_number)
# print(obj3.owner_name1('sonu'))


obj4=SHOP('Rama')
print(SHOP.owner_name('rajdhani','raja'))
print(obj4.get_address("Faridabad"))







