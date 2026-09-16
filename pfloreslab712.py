#Patricia Flores
#Create a python program with the following requirements.
#Ask a user to guess your number by inputing a number
#if the user guesses to within plus or minus 2 of your number, they get another guess and can keep guessing as long as they are within 2 numbers from your number
#if the user guesses your numbger, end the game and display a win message. 
#if the user does not guess your number and is more than 2 away from your number, end the game and display a message that says they lost and if your number was higher or lower. 

#My number is 35
winning_number = 35
number = int(input("Guess my Number:"))



while (number != winning_number and (number - winning_number)<= 2):
   number = int(input("Close, try again"))
    
    
if number == winning_number:
        print ("Well done! You guessed my number:")

elif (number > winning_number):
         print ("Sorry, you lost. Your guess was higher than my number which is ", winning_number)
else:
    print( "Sorry, you lost. Your guess was lower than my number which is ", winning_number)
  


        

     



