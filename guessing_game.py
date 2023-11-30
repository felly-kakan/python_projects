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

   
   



              
