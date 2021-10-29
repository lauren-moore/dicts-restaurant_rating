

def add_restaurant():
    '''ask for new restaurant to add'''
    
    restaurant_name = input("Please type in the restaurant name: ").title()
    return restaurant_name
    
    

def add_score():
    '''ask for new restaurant's score to add'''

    restaurant_score = input("Please type in the restaurant score: ")
    return restaurant_score
    


def rate_restaurant(txt_file):
    """Restaurant rating lister."""

    open_file = open(txt_file)
    scores = {}

    for line in open_file:
        words = line.split(":")

    #add score to dictionary 
        for word in words:  
            scores[words[0]] = int(words[1])
            sorted(scores)
    
    new_name = add_restaurant()
    new_score = add_score()

    #add new restaurant and score to dictionary
    scores[new_name] = int(new_score)

    #alphabetize by restaurant name
    for key, value in sorted(scores.items()):
        print(f"{key} is rated at {value}.")

rate_restaurant("scores.txt")    


