import random #imports a libary which is not apart of the defualt code 
print("__________.__    ")
print("\______   \__| ____   ____  ____   ____     ____   ______ ____ _____  ______   ____  ")
print(" |     ___/  |/ ___\_/ __ \/  _ \ /    \  _/ __ \ /  ___// ___\\__  \ \____ \_/ __ \ ")
print(" |    |   |  / /_/  >  ___(  <_> )   |  \ \  ___/ \___ \\  \___ / __ \|  |_> >  ___/ ")
print(" |____|   |__\___  / \___  >____/|___|  /  \___  >____  >\___  >____  /   __/ \___  >")
print("            /_____/      \/           \/       \/     \/     \/     \/|__|        \/ ")
gameloop=True#this variable makes the activate whent he code is first started 
while gameloop==True:#this is checking to see if the the variable game loop is true
    print("The Pigeons have commited an awful crime against humanity it's your Job to stop them form escaping! Who knows what would happen if they would escape!")#This print function is used to display to the user the backstory of the game so that they can unserstand why they are playing.
    lockcode=input("Enter a valid lockcode between 001 and 100 or type 'QUIT'")#this input is asking the user to enter a valid code or Quit this is then put into the variable lockcode

    
    if lockcode=="QUIT" or lockcode=="quit":#this checks too see if the suer has entered the word quit 
        print("goodbye")#if the user has entered quit it will print the string "goodbye"
        gameloop=False#the game loop will then stop and so will the programme
    else:#if the user has not entered loop it continue the loop
        if len(lockcode)==3:#this checks too see fi the user has entered a valid code which is three characters 
            lockcode=int(lockcode)#this will convert the users input into an integer so that the programme can check to see if it is valid between 1 and 100 

            if lockcode >=1 and lockcode <=100:#the if statment is used to check to see fi the lockcode is valid so that the number is inbetween 1 and 100
                print("lockcode Has Been Entered")#if the lockcode is valid it will print the following message

                guess=0#this resets the variable guess to 0 if the user has already played and is replaying
                tries=0#this resets the variable tries to 0 if the user has already played and is replaying
                maxvalue=100#this assigns the variable max value to 100 so that the escapee can guess a code between 1 and 100
                minvalue=1#this also assigns min variable to 0 so that the escapee has a minium value to gues from

                while guess != lockcode:#this is another loop which is checking to see if the lockcode is not equal to the variable lockcode
                    guess=random.randint(minvalue, maxvalue)#this sets the variable guess to whatever the scapee has guesed fromt he random.randint() fuction
                    tries+=1#once it has guessed it will add one tot he variable tries
                    print("the pigeon guessed", guess)#this indicates to teh suer that the escapee si guessing its code
                    print(minvalue, maxvalue)#debug code


                    if guess==lockcode:#if the escappe has guessed the it will follow this code
                        print("he has escaped it took him", tries, "tries")#this will print to the user that the escapee has escaped and how many tries it took it
                        play_again=input("Do you want to play again? Please enter Yes or No")#this sets the variable play_again fromt he input given from the user
                        if play_again=="yes":#this if statment checks to see if what the user has inputted is equal to yes
                                print("Lets play again")#if so it will display this message stating that they the programme will restart
                        else:#if it is not true this block of code shall be run
                                if play_again=="no" or "No":#this checks to see if the user has entered No or no
                                    print("Goodbye")#if yes the programme will display a message stating that the programe will stop
                                    gameloop=False#this will stop the loop and stop the programme


                    else:#however if the escapee has guessed incorrectly it will follow this code
                        if(guess>lockcode):#if the guess was greater than the lockcode it will follow the indentation
                            maxvalue=guess-1#it will decrease the value of the max value by one

                        else:#if the code is less than the lockde code it will follow this indentation
                            minvalue=guess+1#is the gues was less that the lockcode it will add one to the min value
                    
            else:#if the lockcode is invalid it will follow the indentation
                print("Your lock code is invalid Please Enter a valid code between 1 and 100")#it will print to the user to create a valid lockcode and revert backk to the beginning if the loop to ask for a valid code
        else:#if the lockcode is invalid it will follow the indentation
            print("Your lock code is invalid Please Enter a valid code between 1 and 100")#it will print to the user to create a valid lockcode and revert backk to the beginning if the loop to ask for a valid code


