from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Learn French")
        self.window.config(bg=THEME_COLOR)

        self.my_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, pady=10, padx=10)
        self.my_label.grid(row=0, column=1)
        self.canvas = Canvas(width=500, height=250, bg="white", highlightthickness=0)
        # card_front_img = PhotoImage(file="images/card_front.png")
        self.cards = self.canvas.create_text(250, 100, text="Word", font=("Arial", 20, "italic"), width=450)
        self.canvas.grid(row=1, column=0, columnspan=2)

        my_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=my_image, highlightthickness=0, command=self.user_true)
        self.true_button.grid(row=2, column=0, pady=10, padx=10)

        my_image_1 = PhotoImage(file="images/false.png")
        self.false_button = Button(image=my_image_1, highlightthickness=0, command=self.user_false)
        self.false_button.grid(row=2, column=1)
        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        if self.quiz.still_has_questions():
            next_quest = self.quiz.next_question()
            self.canvas.itemconfig(self.cards, text=next_quest)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.cards, text=f"Quiz finished\nYour score is {self.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.my_label.config(text=f"Score = {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)
