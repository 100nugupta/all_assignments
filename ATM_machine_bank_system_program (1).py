#!/usr/bin/env python
# coding: utf-8

# In[45]:


with open("data.txt", "r") as file:
    for line in file:
        parts= line.strip().split(",")
        if len(parts)!=2:
            #print("Invalid line: ", line)
            continue
        key, value=parts
        print(key,value)
        #store all information in variables
        if key=="Account_number":
            Account_number=int(value)
        elif key=="ATM_pin":
            ATM_pin=int(value)
        elif key=="Account_type":
            Account_type= value
        elif key=="Balance":
            Balance=float(value)
#Now Account holder will give their account details like account number, pin.
acc_num=int(input("enter your account number: "))
user_atm_pin=int(input("Enter your atm_pin: "))

#now we will verify these credentials entered by user
if (acc_num==Account_number) and (user_atm_pin==ATM_pin):
    withdrawl_amount=float(input("Enter the amount that you want to withdrwal: "))
    if withdrawl_amount<=Balance:
        Balance-=withdrawl_amount
        #now we will update the amount in our database.
        with open("data.txt", "w") as file:
            file.write(f"Account_number, {Account_number}")
            file.write(f"ATM_pin, {ATM_pin}")
            file.write(f"Account_type, {Account_type}")
            file.write(f"Balance,{Balance}")
            #Now we will inform the user that you have successfully withdrawn the amount and we will update the file
            print(f"Withdrawl successfull. You remaining balance is:", Balance)
    else:
        print("Insufficient balance in your account.")
else:
    print("Invalid Credentials. Please enter the valid inputs")


    


# In[ ]:





# In[ ]:




