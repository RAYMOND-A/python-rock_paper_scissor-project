import random

# random.seed(123)
# interestingly if we specify a particular seed then the random number generated will
# always be the same

# note that rand module uses the current timestamp as the seed, but we could alway 
# modify the seed
# the randint(a,b) returns random integer number between a and b, with a and b included
random_integer = random.randint(1, 10)
print(random_integer)

# the rand() returns floating point number between 0 and 1, i.e from 0.00000... to 0.9999...
random_float = random.random()
print(random_float)

# creating a random decimal number between 0 and 5, not including 5
random_decimal = random_float * 5
print(random_decimal)

# the concept of the python list, a list is a data structure this is a way we organized
# and store data in python e.g fruits = [items1, items2]

states_of_america = ["Delaware", "Pennsylvania"]

# this prints the first item in the list
print(states_of_america[0])

# this prints the last item in the list
print(states_of_america[-1])

# altering the first item in the list
states_of_america[0] = "New York"
print(states_of_america)

# add an item to the end of list
states_of_america.append("Delaware")
print(states_of_america)

# adding multiples items to the end of the list
states_of_america.extend(["Raymondland", "Akimeland"])
print(states_of_america)

# Nested list
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_frozen = [fruits, vegetables]

print(dirty_frozen)


print("Welcome to the rock paper scissors game")

## Rules of the game
# rock wins against scissors
# scissors wins against paper
# paper wins against rock

rock = '''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

you_choose = choices[your_choice]

print(you_choose)

print("Computer chose")
computer_choice = random.randint(0, 2)

computer_choose = choices[computer_choice]

print(computer_choose)

if your_choice == 0 and computer_choice == 2:
    print("You win")
elif your_choice == 2 and computer_choice == 1:
    print("You win")
elif your_choice == 1 and computer_choice == 0:
    print("You win")
elif you_choose == computer_choose:
    print("Draw")
elif your_choice >= 3 or your_choice < 0:
    print("You lose, you typed an invalid number")
else:
    print("You lose")
