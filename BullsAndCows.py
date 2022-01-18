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
        user_Number = input("Type your 4-digit number:\n>>")    
        if user_Number == "exit":
            print("Sorry to see you leave. See you soon!")
            quit()
        elif len(user_Number) != 4:
            print("Error! You have to enter 4 - digit number") 
        else:
            try:
                user_Number_Check = list(map(int, user_Number))    
            except ValueError:     
                print("Error! You have to enter 4 - digit number")
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
            bulls += 1
        elif x in generated_Number_List and user_Number_Check[check_Place] == generated_Number_List[check_Place]:
            cows += 1
        check_Place += 1

def results():
    global tries
    tries = 0
    while True:
        get_User_Number()
        compare_Numbers()
        print("You have {} cows and {} bulls".format(cows, bulls))
        print()
        if cows == 4:
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
    print("Welcome to the game! Type 'exit' at any time to leave")
    print(generate_Number())
    results()
    play_Again()
    
main()