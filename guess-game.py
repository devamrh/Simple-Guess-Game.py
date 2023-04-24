# Guess Game Mini Project 
print('-------Guess Game Starts -------')

# initial list
init_list = [' ','O',' ']
# shuffle list
from random import shuffle
def shuffle_list(init_list):
    shuffle(init_list)
    shuffled_list = init_list
    return shuffled_list

# User Guess Input
def user_input():
    index = ' '
    while index not in ['0','1','2']:
        index = input('Please guess a number 0,1 or 2\n')
    return int(index)
# Check List

def check_list(shuffled_list,index):
    if shuffled_list[index]== '0':
        print('Correct Guess')
    else:
        print('Wrong Guess')
        print(shuffled_list)
    
#  Now calling all the function below

# Initializing The List
init_list = ['','0','']
# Shuffled List
mixedup_list = shuffle_list(init_list)
# User Input
guess = user_input()
# Check Guess
check_list(mixedup_list,guess)

print('---------Guess Game Ends-------')