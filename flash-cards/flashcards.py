# # flashcards.py
import json

def get_json_deta():
    with open('me-capitals.json', 'r') as f:
        data = json.load(f)
        return data
    
def flashcard_game():
    # get data
    data = get_json_deta()
    # access cards value
    card_list = data["cards"]
    score = 0
    
    for item in card_list:
        
        q = item["q"]
        a = item["a"]
    
        #1 ask user the question and get the answer
        guess = input(q)

        # compare the answer with the json answer
        if a == guess:
            print("u got it")
            score += 1
        else:
            print("try again")
    print(f"Total score= {score} ")
# tell the user their score
        # tell user the result

       
        
    
flashcard_game()
# with open('me-capitals.json', 'r') as f:
    #data = json.load(f)
    #print(data)

# # initialize total as the length of the cards array
# total = len(data["cards"])
# # initialize score as 0
# score = 0

# for i in data["cards"]:
#     guess = input(i["q"] + " > ")

#     if guess == i["a"]:
#         # increment score up one
#         score += 1
#         # interpolate score and total into the response
#         print(f"Correct! Current score: {score}/{total}")
#     else:
#         print("Incorrect! The correct answer was", i["a"])
#         print(f"Current score: {score}/{total}")
        
        
        
# # write funtion that take a nd b, and return the sum
# def sum(a,b):
#     result = a + b
#     return result

# # write a function that take the sum a and b and multiply by 2
# def  multiply (a,b):
#     result = sum(a,b) * 2
#     return result

# # formula to calculate the area of a triangle when you know its base (b) and height (h) is:
# #  0.5 * b * h, write a function that return the area

# def area_triangle():
#     b = int(input("what is the base: "))
#     h = int(input("what is the height: "))
#     result = 0.5 * (b * h)
#     print(result)

# area_triangle()

# score = 3
# score = score + 1 / score +=1
# score -> 4