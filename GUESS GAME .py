import random


# menu function
def menu():
    
    x = int(input(f"\n \t ENTER A NUMBER :\n \t \t 1 : play game \n \t \t 2 : help \n \t \t 0 : exit \n\t"))

    if x==1:
        the_out_no=random.randint(1,6)

        # check= check_guessno(the_out_no) # or youcan use this
        return check_guessno(the_out_no) 

    elif x==2:
        return help()

    elif x==0:  
        exit
    
    else:
        print(f"please enter a valid number ")
        return menu() 

#back function

def back():
    y = int(input(f"Press\n\t'1': to turn back to menu \n\t'0': to exit the game\n\t"))
    
    if y==1:
       return menu()

    elif y==0:  
        exit
    
    else:
        print(f"please enter a valid number ")
        return back()

    


#help function

def help():
    print(f"\nTO PLAY THIS GAME \n \t You must press a number ' 1 ' then it opens the game")
    print(f"\n the game is guessing a number from 1 upto 6. so you should enter your guessing no when the computer asks \n then if you got the number, You won \n but if you did not , you can try upto three times, after three times you fail that is it \n \n\t\t  'HAVE AN ENJOYING GAME' \n")
    return back()

#after you play it display

def gamelast():
    z = int(input(f"Press\n\t'1': to turn back to menu \n\t'3': to continue the game \n\t '0': to exit the game \n\t "))
    
    if z==1:
        return menu()
    
    elif z==3:  
        the_out_no=random.randint(1,6)

        return check_guessno(the_out_no)

    elif z==0:  
        exit
    
    else:
        print(f"please enter a valid number \n")
        return gamelast() 

#def play game function

def check_guessno(the_out_no):

    for count in range(1,4):

        your_Entered_no=input(f"\n \tGuess a number from 1 up to 6:\n \t\t")
        print(f"\n\tYour_Entered_no is:\n \t \t {your_Entered_no}  ")

        if the_out_no ==int(your_Entered_no):
            print(f"\n\t YOU GOT , The no is {the_out_no}")
            print(f"\t CONGRATULATION.... YOU WON !!! \n ")

            break

        else:

            if count<3:
                #print(f"the out no is {the_out_no} and your guess number is {your_Entered_no}")
                print(f"\n\tSorry...You lost Please GUESS again...")  

            else:
                print(f"\n\t You tried three times but you did not get,The no. is :{the_out_no} \n\t THE GAME IS OVER !!! \n \t\t GOOD BYE\n")   
    
    #after plays game function
    gamelast()
    

   


print(f"\n\t WELCOME TO GUESS GAME\n")

menu()
# m=menu() #you can use this