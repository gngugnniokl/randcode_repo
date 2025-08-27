import random

question = "What is your favourite type of weather? "
user_input = input(question)

scrambled = ''.join(random.sample(user_input, len(user_input)))
print("Scrambled letters:", scrambled)