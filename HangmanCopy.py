import tkinter as tk
import random

class Hangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")

        # List of words for game to randomly select
        self.words = ["door", "bird", "turtle", "stone", "balloon", "camera",
                      "bottle", "monitor", "keyboard", "record"]
        self.word = random.choice(self.words)
        self.guesses = set()
        self.attempts = 6
        self.remainingAttempts = self.attempts
        self.guessCorrect = set()

        # Gui stuff
        self.displayedWord = tk.Label(root, text=self.getWord(), font = ('Arial', 24))
        self.displayedWord.pack(pady = 20)

        self.guessLabel = tk.Label(root, text = "Enter a letter:", font = ('Arial', 14))
        self.guessLabel.pack()

        self.userGuess = tk.Entry(root, font = ('Arial', 14))
        self.userGuess.pack(pady = 10)

        self.guessButton = tk.Button(root, text = "Guess", font=('Arial', 14), command=self.makeGuess)
        self.guessButton.pack(pady = 10)

        self.attemptsDisplay = tk.Label(root, text=f"Attempts left: {self.remainingAttempts}", font=('Arial', 14))
        self.attemptsDisplay.pack(pady = 10)

        self.textLabel = tk.Label(root, text = "", font = ('Arial', 14))
        self.textLabel.pack(pady = 10)

    # Gets the randomly selected word
    def getWord(self):
        return " ".join([letter if letter in self.guessCorrect else "_" for letter in self.word])

    # Creates the user's guessed letter
    def makeGuess(self):
        guess = self.userGuess.get().lower()
        self.userGuess.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.textLabel.config(text = "Enter a single letter.")
            return

        if guess in self.guesses:
            self.textLabel.config(text = "Cannot guess a lette more than once.")
            return

        self.guesses.add(guess)

        if guess in self.word:
            self.guessCorrect.add(guess)
            self.textLabel.config(text = "Correct!")
        else:
            self.remainingAttempts -= 1
            self.textLabel.config(text = "Incorrect!")
        
        self.progressGame()

    def progressGame(self):
        # Updates the displayed word
        self.displayedWord.config(text = self.getWord())
        self.attemptsDisplay.config(text = f"Attempts left: {self.remainingAttempts}")

        # Checks if game has ended
        if set(self.word) == self.guessCorrect:
            self.textLabel.config(text = "Congratulations! The word was: " + self.word)
            self.guessButton.config(state = tk.DISABLED)
        elif self.remainingAttempts <= 0:
            self.textLabel.config(text = f"You lose! The word was: {self.word}. Sorrgy, try again.")
            self.guessButton.config(state = tk.DISABLED)

# Creates a main window
root = tk.Tk()

# Creates and runs the game itself
game = Hangman(root)
root.mainloop()