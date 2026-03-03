class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word +'(' + self.meaning + ')'
flash = []
print("Welcome to flashcard app!\n")
while True:
    word = input("Enter a word: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(Flashcard(word, meaning))
    option = int(input("Do you want to add more flashcards? (1 for yes, 0 for no):\n"))
    if not option:
        break
print("Your flashcards:")
for i in flash:
    print(">",i)