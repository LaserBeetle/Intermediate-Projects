import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tkinter.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="Placeholder", font=("Arial", 15, "italic"),
                                                fill=THEME_COLOR, width=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.right = tkinter.Button(command=self.true_pressed)
        self.true = tkinter.PhotoImage(file="images/true.png")
        self.right.config(image=self.true, highlightthickness=0)
        self.right.grid(column=0, row=2)

        self.wrong = tkinter.Button(command=self.false_pressed)
        self.false = tkinter.PhotoImage(file="images/false.png")
        self.wrong.config(image=self.false, highlightthickness=0)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
