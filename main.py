import random

'''
1  for snake
-1 for water
0 for gun
'''
# computer=-1 here value is fixed
computer=random.choice([-1,0,1]) #here computer will automatically choose

youstr=input("enter your choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

if youstr not in youdict:
    print("Invalid choice! Enter s, w, or g.")
    exit()


you=youdict[youstr]
print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer==you):
    print("its a draw!")

else:
   if(computer==-1 and you==1):
    print("you win!")
   elif(computer==-1 and you==0):
    print("you lose!")

   elif(computer==1 and you==-1):
    print("you lose!")
   elif(computer==1 and you==0):
    print("you win!")

   elif(computer==0 and you==-1):
    print("you lose!")
   elif(computer==0 and you==1):
    print("you win!")

   else:
    print("something went wrong")