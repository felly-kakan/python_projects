
def send_money():
    while True:
        phone_number=input("Enter  phone number: ")
        # Remove any non-digit characters from the input
        phone_number = ''.join(char for char in phone_number if char.isdigit())
        if len(phone_number)==10:
         #   print("good")
           break 
        else:
           print("Invalid phone number!Check your phone number") 

    while True:
        amount_str=input("Enter amount: ")
        if amount_str.isdigit():
           amount=int(amount_str)
        
           if   amount>0 and amount<=200000:
            #   print("proceed !")
              break
          
           else:
              print("amount is more or less than expected! please check entered amount")
                
        else: 
         print("amount shld be numbers")


    while True:
      pin=input("Enter pin: ")
      if pin.isdigit() and  len(pin)==4:
            print("money send successfully")
            break
      else:
                 print("pin shld contain 4 numbers") 


 
#send_money()          