import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

r = requests.get('http://hf-food.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+Dining%3a+J2+%26+JCL&naFlag=1', headers = headers)

content = r.content

soup = BeautifulSoup(content, features="lxml")

meals = {}
index = 0


validChoices = ['breakfast', 'lunch', 'dinner']

#gets the columns for the 3 meal - Breakfast, Lunch, and Dinner
for lunchTime in soup.find_all("td", attrs = {"valign": "top", "width": "30%"}):
    wordsList = []

    for word in lunchTime.stripped_strings:
        wordsList.append(word)

    recipiesAtMeal = []
    for index in range(1, len(wordsList)):
        currWord = wordsList[index]
       
        recipiesAtMeal.append(wordsList[index])


    meals[wordsList[0].lower()] = recipiesAtMeal




# returns a valid user choice 
def checkValidUserInput():
    validChoices = ['breakfast', 'lunch', 'dinner']
    valid = False
    userInput = ""
    while not valid:
        userInput = input("Do you want to see 'Breakfast', 'Lunch', or 'Dinner'?\n")
        userInput = userInput.lower()
        if userInput in validChoices:
            valid = True
        else:
            print("Invalid choice. Please type 'Breakfast', 'Lunch', or 'Dinner'")
    
    return userInput

#outputs the meal given a user input
def outputMeals(userInput):
    for meal in meals[userInput]:
        if '-' in meal:
            meal = meal.replace('-',"")
            print("\nFor " + meal + " there is: ")
        else:
            print("\t" + meal)
        



userInput = checkValidUserInput()

outputMeals(userInput)



        

        


