#Welcoming the Player to the game 
print("Welcome to the Game :) ")

#Asking player if he wants to play the game or not
answer=input("Do you want to play the game\nYes or no ?\n")

#if user says yes then we will continue with the game or else the game will end 
if answer.lower()!="yes":#.lower method to get the user input in lower alphabets
    print("See you Again")
    quit()
    
print("Let's Start the game!")
right_ans=0
wrong_ans=0

#Question number1
print("Question number 1 ")
answer=input("GPU stands for ?\n")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    right_ans+=1
else:
    print("Incorrect")
    wrong_ans+=1
    
#Question number2      
print("Question number 2 ")
answer=input("CPU stands for ?\n")
if answer.lower()=="central processing unit":
    print("Correct!")
    right_ans+=1
else:
    print("Incorrect")
    wrong_ans+=1
    
#Question number3    
print("Question number 3 ")
answer=input("API stands for ?\n")
if answer.lower()=="application programming unit":
    print("Correct!")
    right_ans+=1
else:
    print("Incorrect")
    wrong_ans+=1
    
#Question number4    
print("Question number 4 ")
answer=input("DBMS stands for ?\n")
if answer.lower()=="database management system":
    print("Correct!")
    right_ans+=1
else:
    print("Incorrect")
    wrong_ans+=1
    
#Question number5
print("Question number 5 ")
answer=input("RAM stands for ?\n")
if answer.lower()=="random access memory": 
    print("Correct!")
    right_ans+=1
else:
    print("Incorrect")
    wrong_ans+=1
    
#Printing the Score of the User
#Using F string method
print(f"you got {right_ans} answer correct and {wrong_ans} answers wrong out of 5")
#printing out the percentage of right answer
print("you got ",(right_ans/5)*100,"%")