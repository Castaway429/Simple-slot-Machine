import random
import time
from colorama import Fore, Style
balance = 99999
balance = int(balance)
ICONS = ["Cherry", "Seven", "HorseShoe", "Bell", "Bar", "Heart", "Watermelon", "Lemon", "Diamond"]

firstWheel = None
secondWheel = None
thirdWheel = None

def spinWheel():
        Rnumber = (random.randint(0,8))
        return ICONS[Rnumber]

def printScore():
        # DECREASE BY 4% LATER
        global balance, firstWheel, secondWheel, thirdWheel
        if ((firstWheel == "Cherry") and (secondWheel == "Cherry") or (secondWheel == "Cherry") and (thirdWheel == "Cherry")) :
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "HorseShoe") and (secondWheel == "HorseShoe") or (secondWheel == "HoreShoe") and (thirdWheel == "HoreShoe")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1          
        elif ((firstWheel == "Bar") and (secondWheel == "Bar") or (secondWheel == "Bar") and (thirdWheel == "Bar")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Heart") and (secondWheel == "Heart") or (secondWheel == "Heart") and (thirdWheel == "Heart")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Watermelon") and (secondWheel == "Watermelon") or (secondWheel == "Watermelon") and (thirdWheel == "Watermelon")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Lemon") and (secondWheel == "Lemon") or (secondWheel == "Lemon") and (thirdWheel == "Lemon")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Diamond") and (secondWheel == "Diamond") or (secondWheel == "Diamond") and (thirdWheel == "Diamond")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Bell") and (secondWheel == "Bell") or (secondWheel == "Bell") and (thirdWheel == "Bell")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif ((firstWheel == "Seven") and (secondWheel == "Seven") or (secondWheel == "Seven") and (thirdWheel == "Seven")):
            balance = balance + bet + (12 * bet / 100)
            print("{:.2f}".format(balance))  # NORMAL
            win = 1
        elif((firstWheel == "Cherry") and (secondWheel == "Cherry") and (thirdWheel == "Cherry")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "HorseShoe") and (secondWheel == "HoreShoe") and (thirdWheel == "HoreShoe")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Bell") and (secondWheel == "Bell") and (thirdWheel == "Bell")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Bar") and (secondWheel == "Bar") and (thirdWheel == "Bar")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Watermelon") and (secondWheel == "Watermelon") and (thirdWheel == "Watermelon")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Lemon") and (secondWheel == "Lemon") and (thirdWheel == "Lemon")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Diamond") and (secondWheel == "Diamond") and (thirdWheel == "Diamond")):
            balance = balance + bet + (20 * bet / 100)
            print("{:.2f}".format(balance))  # UNIQUE
            win = 1
        elif((firstWheel == "Seven") and (secondWheel == "Seven") and (thirdWheel == "Seven")):
            balance = balance + bet + (100 * bet / 100)
            print("{:.2f}".format(balance))  # JACKPOT
            win = 2
        else: 
            win = -1
        
        if win > 0:
            print("|" + firstWheel + " , " + secondWheel + " , " + thirdWheel + "| !" + Fore.GREEN + " YOU WON!" + Style.RESET_ALL + " Your new balance is $" + Fore.GREEN + str(balance) + Style.RESET_ALL + ".")
        elif win > 1:
            print("|" + firstWheel + " , " + secondWheel + " , " + thirdWheel + "| !" + Fore.GREEN + " YOU WON THE JAKPOT!" + Style.RESET_ALL + " Your new balance is $"+ Fore.GREEN + str(balance) + Style.RESET_ALL + ".")
        else:
            print("|" + firstWheel + " , "+ secondWheel + " , " + thirdWheel +"| !"+ Fore.RED + " YOU LOST!!" + Style.RESET_ALL + " Your new balance is $" + Fore.RED + str(balance) + Style.RESET_ALL + ".")
    
print("You wander upon a Casino door open? (" + Fore.YELLOW + "yes" + Style.RESET_ALL + " / " + Fore.YELLOW + "no" + Style.RESET_ALL + ")")
while balance == 99999:
    enter = input()
    if enter.lower() == "yes" :
        print("Welcome to THE Casino!")
        time.sleep(2)
        print("The door suddently locks behind you and scary guards appear! They say you must earn 1 MILLION Dollars to leave!")
        time.sleep(4)
        print("You check your pockets")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("You only have $100000 dollars. You walk to the nearest Slot Machine and begin pulling...")
        balance = balance + 1
        time.sleep(1)
    elif enter.lower() == "no":
        print("Congrats! You saved yourself from a crippling addiction, ungodly amounts of debt, and being kidnapped! :)")
        break
    else:
        print(Fore.RED + "ERROR: INVALID INPUT ONLY 'YES' or 'NO'" + Style.RESET_ALL)

while balance >= 100000:
    print("Your balance is $" + Fore.GREEN + str(balance) + Style.RESET_ALL + ". Would you like to play? (" + Fore.YELLOW + "Yes" + Style.RESET_ALL + " or " + Fore.YELLOW + "No" + Style.RESET_ALL + ")")
    answer = input()
    answer = answer.lower()
    if answer == "yes":
        while True:
            if balance == 0:
                print(Fore.RED +"GAME OVER: RAN OUT OF MONEY!")
                break
            print("How much do you want to bet?")
            bet = input()
        
            if bet.isalpha(): 
                print(Fore.RED + "ERROR: ONLY NUMBERS ALLOWED" + Style.RESET_ALL)
                break
            elif "$" in bet:
                print(Fore.RED + "ERROR: ONLY NUMBERS ALLOWED" + Style.RESET_ALL)
                continue
            elif "-" in bet:
                  print(Fore.RED + "ERROR: NO NEGATIVES ALLOWED" + Style.RESET_ALL)
                  continue
            else: 
                bet = int(bet)
            if bet > balance:
                print(Fore.RED + "WHOA! You don't have that kind of money!" + Style.RESET_ALL)
            elif bet <= balance:
                balance = int(balance) - int(bet)
                #print(Fore.GREEN + str(balance) + Style.RESET_ALL)
                firstWheel = spinWheel()
                secondWheel = spinWheel()
                thirdWheel = spinWheel()
                printScore()

 
    elif answer == "no":
        print(Fore.RED +"ARE YOU SURE YOU WANT TO GIVE UP? " + Style.RESET_ALL + Fore.YELLOW +"(yes / no)" + Style.RESET_ALL)
        end = input()
        if end == "yes":
            print("You give up I guess. You now live in this casion. You ended with $" + str(balance))
            break
        elif end == "no":
            continue
        else:
            print(Fore.RED + "ERROR: UNRECOGNIZED INPUT" + Style.RESET_ALL)

while balance >= 1000000:
    print("Win :)! Congrats you're really good! Bye!")
    break