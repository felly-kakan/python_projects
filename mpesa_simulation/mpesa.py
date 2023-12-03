
from sendmoney import send_money
import withdrawmoney 
# withdrawmoney.withdraw

def main_menu():
        print('''
1:Send money 
2:withdraw
0:cancel                                                     
''')
  
while True:
    main_menu()
    selection=int(input("Enter your choice: ")) 
    if selection==1:
      send_money()
      break
    
    elif selection==2:
        print('''
    1: Agent
    2: Bank

''')
        choice=int(input("Enter your choice "))

        if choice==1:
            withdrawmoney.agent()
            break

        elif choice==2:
            withdrawmoney.bank()
        # payment_methods.bank()
            break
        else:
            print("invalid choice!try again")
            break



    elif selection == 0:
        print("Operation canceled.")
        break

    
    else:   
     print("invalid choice")     
           

