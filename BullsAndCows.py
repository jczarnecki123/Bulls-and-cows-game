import random

def generate_number():
    global generated_number_list
    generated_number_list = []
    while len(generated_number_list) != 4:
        generated_number = random.randint(0,9)
        if generated_number not in generated_number_list:
            generated_number_list.append(generated_number)
    return generated_number_list

def get_user_number():
    global user_number_check
    while True:
        count_number_check = 0
        user_number = input("Type your 4-digit number:\n>>")    
        if user_number == "exit":
            print("Sorry to see you leave. See you soon!")
            quit()
        elif user_number == "rules":
            with open("d:/code/Bulls and cows game/rules.txt", "r") as f:
                for line in f:
                    print(line)
        elif len(user_number) != 4:
            print("Error! You have to enter 4 - digit number\n") 
        else:
            try:
                user_number_check = list(map(int, user_number))    
            except ValueError:     
                print("Error! You have to enter 4 - digit number\n")
            else:
                for number in user_number_check:
                    count_Number = user_number_check.count(number)
                    if count_Number != 1:
                        count_number_check += 1
                if count_number_check != 0:
                    print("Careful! The number you are trying to guess is never going to have the same 2 digits. Try again\n")
                else: 
                    break

def compare_numbers():
    global cows, bulls, tries
    tries += 1
    bulls = 0
    cows = 0
    check_place = 0
    for x in user_number_check:
        if x in generated_number_list and user_number_check[check_place] != generated_number_list[check_place]:
            cows += 1
        elif x in generated_number_list and user_number_check[check_place] == generated_number_list[check_place]:
            bulls += 1
        check_place += 1

def results():
    global tries
    tries = 0
    while True:
        get_user_number()
        compare_numbers()
        print("You have {} bulls and {} cows".format(bulls, cows))
        print()
        if bulls == 4:
            print("Congratulations! You win \nIt took you {} tries to get the right number".format(tries))
            break

def play_again():
    ask_user = input("Do you want to play again?\n[Yes]/[No]")
    if ask_user.lower() == "yes":
        main()
    elif ask_user.lower() == "no" or ask_user.lower() == "exit":
        quit()
    else:
        print("Error! You have to type 'Yes' or 'No'")
        play_again()

def main():
    print("Welcome to the game! Type 'exit' at any time to leave. If you want to read rules, type [rules]. Also you can exit at any time you want, just type [exit].")
    print(generate_number()) #<-- for dev only
    results()
    play_again()
    
main()