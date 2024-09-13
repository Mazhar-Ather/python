# this program create kon bany ga crore pati
import sys
lis1=["how many seasons are in pakistan?","2","3","4","5","c"]
lis2=["what is the capital of pakistan?","lahore","islamabad","multan","sakardu","b"]
lis3=["Who is the my best friend","adeel","haseeb","amina","areeba","c"]
lis4=["Qno1) ","a) ","b) ","c) ","d) "]

for i in range(0,5):
    print(lis4[i],lis1[i])

ans=input("Enter correct option: ")
if ans == lis1[5]:
    print("You win 10k")
if ans != lis1[5]:
    print("you lost, better luck next time")
    sys.exit()
    
con=input("do you want to continue? \n press y for continue \n press n for quit")
if con=="n":
    print("You win 10k. Good Bye")
else:
   print("next question")
   for i in range(0,5):
    print(lis4[i],lis2[i])

ans=input("Enter correct option: ")
if ans == lis2[5]:
    print("You win 50k")
if ans != lis2[5]:
    print("you lost, better luck next time")
    sys.exit()
    
con=input("do you want to continue? \n press y for continue \n press n for quit")
if con=="n":
    print("You win 50k. Good Bye")
else:
    print("next question")
    for i in range(0,5):
       print(lis4[i],lis3[i])

ans=input("Enter correct option: ")
if ans == lis3[5]:
    print("You win 100k")
if ans != lis3[5]:
    print("you lost, better luck next time")
    sys.exit()


