import random

def generate_Number():
    global generated_Number_List
    generated_Number_List = []
    while len(generated_Number_List) != 4:
        generated_Number = random.randint(0,9)
        if generated_Number not in generated_Number_List:
            generated_Number_List.append(generated_Number)
    return generated_Number_List

def get_User_Number():
    global user_Number_Check
    while True:
        count_Number_Check = 0
        user_Number = input("Type your 4-digit number:\n>>")    
        if user_Number == "exit":
            print("Sorry to see you leave. See you soon!")
            quit()
        elif user_Number == "rules":
            with open("d:/code/Bulls and cows game/rules.txt", "r") as f:
                for line in f:
                    print(line)
        elif len(user_Number) != 4:
            print("Error! You have to enter 4 - digit number\n") 
        else:
            try:
                user_Number_Check = list(map(int, user_Number))    
            except ValueError:     
                print("Error! You have to enter 4 - digit number\n")
            else:
                for number in user_Number_Check:
                    count_Number = user_Number_Check.count(number)
                    if count_Number != 1:
                        count_Number_Check += 1
                if count_Number_Check != 0:
                    print("Careful! The number you are trying to guess is never going to have the same 2 digits. Try again\n")
                else: 
                    break

def compare_Numbers():
    global cows, bulls, tries
    tries += 1
    bulls = 0
    cows = 0
    check_Place = 0
    for x in user_Number_Check:
        if x in generated_Number_List and user_Number_Check[check_Place] != generated_Number_List[check_Place]:
            cows += 1
        elif x in generated_Number_List and user_Number_Check[check_Place] == generated_Number_List[check_Place]:
            bulls += 1
        check_Place += 1

def results():
    global tries
    tries = 0
    while True:
        get_User_Number()
        compare_Numbers()
        print("You have {} bulls and {} cows".format(bulls, cows))
        print()
        if bulls == 4:
            print("Congratulations! You win \nIt took you {} tries to get the right number".format(tries))
            break

def play_Again():
    ask_User = input("Do you want to play again?\n[Yes]/[No]")
    if ask_User.lower() == "yes":
        main()
    elif ask_User.lower() == "no" or ask_User.lower() == "exit":
        quit()
    else:
        print("Error! You have to type 'Yes' or 'No'")
        play_Again()

def main():
    print("Welcome to the game! Type 'exit' at any time to leave. If you want to read rules, type 'rules'")
    print(generate_Number()) #<-- for dev only
    results()
    play_Again()
    
main()