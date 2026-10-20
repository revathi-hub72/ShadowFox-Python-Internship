#Task 5: For Loop

import random

# Program 1: Roll a six-sided die 20 times
ones = 0
sixes = 0
consecutive_sixes = 0
previous_was_six = False

print("Die roll results:")

for i in range(20):
    roll = random.randint(1, 6)
    print(roll, end=" ")

    if roll == 1:
        ones += 1

    if roll == 6:
        sixes += 1

    if roll == 6 and previous_was_six:
        consecutive_sixes += 1

    previous_was_six = (roll == 6)

print("\nNumber of ones:", ones)
print("Number of sixes:", sixes)
print("Consecutive pairs of sixes:", consecutive_sixes)

# Program 2: 100 Jumping Jacks
for set_number in range(1, 11):
    print("\nComplete set", set_number, "- 10 jumping jacks.")

    if set_number < 10:
        tired = input("Are you tired? (yes/no): ").strip().lower()

        if tired == "yes":
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()

            if skip == "yes":
                print("You completed", set_number * 10, "jumping jacks.")
                break
            else:
                print("Continue exercising!")
else:
    print("Congratulations! You completed 100 jumping jacks.")


