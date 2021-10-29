



            
    



def rate_restaurant(txt_file):
    """Restaurant rating lister."""

    open_file = open(txt_file)
    scores = {}

    for line in open_file:
        words = line.split(":")

    #add score to dictionary 
        for word in words:  
            scores[words[0]] = int(words[1])
            
    
    #new_name = add_restaurant()
   # new_score = add_score()

    #add new restaurant and score to dictionary
   # scores[new_name] = new_score
    
    return scores
    #alphabetize by restaurant name
    for key, value in sorted(scores.items()):
        print(f"{key} is rated at {value}.")

    

def add_restaurant():
    '''ask for new restaurant to add'''
    
    restaurant_name = input("Please type in the restaurant name: ").title()
    return restaurant_name
    
    

def add_score():
    '''ask for new restaurant's score to add'''

    while True:

        restaurant_score = int(input("Please type in the restaurant score: "))

        if restaurant_score > 5 or restaurant_score < 1:
            print("Invalid score. Maximum score is 5")

        else:
            return restaurant_score


def adding_new_restaurant():
    rate_restaurant("scores.txt")
    new_n
    new_score = add_scores()

    #add new restaurant and score to dictionary
    
    scores[new_name] = new_score
   


def give_choices():
    while True:

        user_choice = input("A. See all current ratings.\nB. Add a new restaurant and rating.\nC. Quit.\n\nWhat would you like to do? ").upper()
            #seeing all the rating
        if user_choice == "A":
            rate_restaurant("scores.txt") 
            print()
            
        #adding a new restaurant (and rate)
        elif user_choice == "B":
            add_restaurant() 
            add_score()
            adding_new_restaurant()
            
            print()
            
        #quitting
        elif user_choice == "C":
            print("Goodbye!")
            break
        
        else:
            print("Wrong choice. Please choose again!")

give_choices()