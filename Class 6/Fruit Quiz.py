import random
class FruitQuiz:
    def __init__(self):
        self.highscore = 0
        self.fruits = {'apple':'red',
                       'banana':'yellow',
                       'watermelon':'green',
                       'orange':'orange',
                       'grape':'purple',
                       'kiwi':'brown',
                       'blueberry':'blue',
                       'lemon':'yellow',
                       'strawberry':'red',}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of", fruit, "?")
            answer = input("Your answer: ")
            if answer.lower() == color:
                print("Correct!")
                self.highscore += 1
            else:
                print("Wrong! The correct answer is", color)
                break
            option = int(input("Do you want to continue? (1 for yes, 0 for no):\n"))
            if not option:
                print("Your streak is:", self.highscore)
                break
print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()        