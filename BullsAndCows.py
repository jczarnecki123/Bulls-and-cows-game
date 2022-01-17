import random
# from winreg import CloseKey

def generate_Number():
    global generated_Number_List
    generated_Number_List = []
    while len(generated_Number_List) != 4:
        generated_Number = random.randint(0,9)
        if generated_Number not in generated_Number_List:
            generated_Number_List.append(generated_Number)
    return generated_Number_List

def compare_Numbers():
    tries = 0
    while True:
        bulls = 0
        cows = 0
        user_Number = input("Type your 4-digit number:\n>>")
        if len(user_Number) != 4:
            print("Error! You have to enter 4 - digit number")
        else:
            tries += 1
            user_Number_Check = list(map(int, user_Number))
            check_Place = 0
            for x in user_Number_Check:
                if x in generated_Number_List and user_Number_Check[check_Place] != generated_Number_List[check_Place]:
                    bulls += 1
                elif x in generated_Number_List and user_Number_Check[check_Place] == generated_Number_List[check_Place]:
                    cows += 1
                check_Place += 1
            print("You have {} cows and {} bulls".format(cows, bulls))
            print()
            if cows == 4:
                print("Congratulations! You win \nIt took you {} tries to get the right number".format(tries))
                break

def play_Again():
    ask_User = input("Do you want to play again?\n[Yes]/[No]")
    if ask_User.lower() == "yes":
        main()
    elif ask_User.lower() == "no":
        quit()
    else:
        print("Error! You have to type 'Yes' or 'No'")
        play_Again()

def main():
    print("Welcome to the game!")
    print(generate_Number())
    compare_Numbers()
    play_Again()
    
main()