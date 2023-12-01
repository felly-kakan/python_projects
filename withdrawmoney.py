# from payment_methods import agent ,bank
#NB(you can import the payment_method module to withdraw money 
# or intialize the functions before calling them  but make sure you indent  while loop for it inner loop)



def agent():
        print("agent")
        while True:
            agent_str=input("Enter agent number ")
            if agent_str.isdigit() and len(agent_str)>=4:
        # print("continue") 
              break
            else:
              print("please enter correct agent and should be more or equal to 4 digits") 

        while True: 
            amount_str=input("Enter amount ")
            if amount_str.isdigit():
                amount=int(amount_str)
                if amount>0 and amount<=200000:
            # print("proceed")
                   break

                else:
                    print("amount is more or less than expected! please check entered amount")   

            else:
                 print("amount shld be number") 

#get pin  
        while True:
            pin_str=input("Enter your pin ")
            if pin_str.isdigit() and len(pin_str)==4:
               print("money withdrawn successfully")
               break
            else:
               print("pin shld contain 4 numbers") 
def bank():
        print("bank")  
        while True:
            bank_account_str=input("Enter your bank account  number ")
            if bank_account_str.isdigit() and len(bank_account_str)>=10:
            # print("continue") 
                break
            else:
                print("please enter correct bank account and should be more or equal to 10 digits") 

        while True: 
            amount_str=input("Enter amount ")
            if amount_str.isdigit():
                amount=int(amount_str)
                if amount>0 and amount<=200000:
                # print("proceed")
                   break

                else:
                    print("amount is more or less than expected! please check entered amount")   

            else:
                print("amount shld be number")

        #get pin  
        while True:
            pin_str=input("Enter your pin ")
            if pin_str.isdigit() and len(pin_str)==4:
               print("money  successfully deposited in bank")
               break
            else:
                print("pin shld contain 4 numbers")   







              


