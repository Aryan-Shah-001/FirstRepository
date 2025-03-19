import random

NumberOfTimeToBeExecuted = int(input("Enter the number to time the program has to be executed: "))

while True:
    a = input("Enter the object (Dice OR Coin): ").lower()

    if a == "coin":
        No_of_heads = 0
        No_of_tails = 0

        Probability = ["H", "T"]

        for i in range(0, NumberOfTimeToBeExecuted):
            ChoiceIs = random.choice(Probability)

            if ChoiceIs == "H":
                No_of_heads += 1
            elif ChoiceIs == "T":
                No_of_tails += 1

        print(f"Number of heads is '{No_of_heads}' and \nNumber of tails is '{No_of_tails}'")

        break

    elif a == "dice":
        No_of_1 = 0
        No_of_2 = 0
        No_of_3 = 0
        No_of_4 = 0
        No_of_5 = 0
        No_of_6 = 0

        Probability = [1, 2, 3, 4, 5, 6]

        for i in range(0, NumberOfTimeToBeExecuted):
            Choice2 = random.choice(Probability)

            if Choice2 == 1:
                No_of_1 += 1
            elif Choice2 == 2:
                No_of_2 += 1
            elif Choice2 == 3:
                No_of_3 += 1
            elif Choice2 == 4:
                No_of_4 += 1
            elif Choice2 == 5:
                No_of_5 += 1
            elif Choice2 == 6:
                No_of_6 += 1

        print(f"No. of 1(s) are {No_of_1}")
        print(f"No. of 2(s) are {No_of_2}")
        print(f"No. of 3(s) are {No_of_3}")
        print(f"No. of 4(s) are {No_of_4}")
        print(f"No. of 5(s) are {No_of_5}")
        print(f"No. of 6(s) are {No_of_6}.")

        break
