from turtle import Turtle
import pyttsx3
import winsound
import random

game_over = ['nice try', 'better luck next time', 'can do more better', 'i appreciate for your try', 'great play',
             'well played']

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak(audio):
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        random_words_to_end_game = random.choice(game_over)
        speak("GAME OVER.") 
        print(f"{random_words_to_end_game}")
        speak(f"{random_words_to_end_game}")

    def increase_score(self):
        self.score += 1
        winsound.PlaySound("Water_drop.mp3", winsound.SND_ASYNC)
        self.clear()
        self.update_scoreboard()
