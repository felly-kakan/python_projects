

# Select the Block of Code:
# Select the block of code that you want to indent.

# Use the Tab Key:
# Press the "Tab" key on your keyboard to indent the selected block of code.

# Use Shift + Tab to Unindent:
# If you want to decrease the indentation, use "Shift + Tab."
import random

def guess_game():
   computer=random.randint(1,10)
   print(computer)

   attempts=0
   attempts_limit=3

   while attempts<attempts_limit:
      attempts+=1

      player=int(input("Guess "))
      if player==computer:
         print(f"computer random guess= {computer}")
         print("youve won")
   else:
      print(f"computer random guess= {computer}")
      print("youve lost")      
      

   
guess_game()

   
   



              
