import random
print("Welcome!")
print("Are you ready for a game of hangman?")
list1=["maple","peach","pear","dragonfruit","mango","pineapple","plum","watermelon","grapes","kiwi","banana","orange","sweetlime"]
str1=random.choice(list1)
l1=len(str1)
guess=""
print("Here is your word:")
for i in range(0,l1):
  guess+="?"
print(guess)
life=0
final=guess
while(life<6):
  if(life==4):
    print("Sorry, you are out if guesses.The word was",str1.upper(),",you can try playing again!")
    break
  elif(guess==str1):
    print("Congratuations! You have guessed the word",str1.upper(),"correctly!")
    break
  else:
    g=input("Enter your guess:")
    if(g in str1):
      print("Correct guess!")
      for x in range(0,len(str1)):
         if(g==str1[x]):
           guess=guess[0:x]+g+guess[x+1:len(str1)+1]
      print(guess)
    elif(g not in str1):
     print("Incorrect guess!")
     print("You have ",(3-life)," guess(es) remaining")
     life+=1
  
