import random

round_count :int  = 1
score :int = 0

def main():
    global round_count , score

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    while round_count > 0 and round_count < 6:
      print(f"Round {round_count}\n ")
      round_count += 1

      your_number = random.randint(1,100)
      computer_number = random.randint(1,100)
      print(f"Your number : {your_number}")
    #   print(f"computer number  : {computer_number}")

      choice = input("Is computer number is higher or lower than Your number Enter only \"Higher or lower\" : ")


      if choice.lower() == 'higher' or choice.lower() =='lower' :
          Is_true  = choice.lower() =='lower' and your_number > computer_number
          Is_false = choice.lower() =='higher' and your_number < computer_number

          if Is_true or Is_false :
            print(f"You Guess is Right . computer number is {computer_number}")
            score += 1
            print(f"Your Score is {score}\n")

          else:
            print(f"You Guess is Wrong . computer number is {computer_number}")
      else :
        print("Invalid Input")

    if score == round_count:
      print(f"You Played perfectly and your Score : {score}")
    elif score < round_count :
      print(f"You played nice and your score : {score}")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
