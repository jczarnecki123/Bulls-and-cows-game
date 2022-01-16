import random
# from winreg import CloseKey

def generate_Number():
    global generated_Number
    generated_Number = []
    for x in range(0, 4):
        generated_Number.append(random.randint(0,9))
    return generated_Number

def compare_Numbers():
    tries = 0
    while(True):
        tries += 1
        bulls = 0
        cows = 0
        user_Number = input("Type your number:\n>>")
        user_Number_Check = list(map(int, user_Number))
        check_Place = 0
        for x in user_Number_Check:
            if x in generated_Number and user_Number_Check[check_Place] != generated_Number[check_Place]:
                bulls += 1
            elif x in generated_Number and user_Number_Check[check_Place] == generated_Number[check_Place]:
                cows += 1
            check_Place += 1
        print("You have",cows,"cows and",bulls,"bulls")
        if cows == 4:
            print("Congratulations! You win \nIt took you",tries,"tries to get the right number")
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