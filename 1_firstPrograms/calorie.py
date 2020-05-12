# Challenge - Calorie Counter

# Input responses from the user
print("Today's date?")
date = input()
print("Breakfast calories?")
breakfast = int(input())
print("Lunch calories?")
lunch = int(input())
print("Dinner calories?")
dinner = int(input())
print("Snack calories?")
snack = int(input())

# Calculate and displat total daily calories
total = breakfast + lunch + dinner + snack
print("Calorie content for " + date + ": " + str(total))