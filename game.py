import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("2025 Quiz of Uagadou Academy of Magic")
        self.root.geometry("500x400")

        # Initialize scores
        self.scores = {"Ingonyame": 0, "Umkhombe": 0, "Indlovu": 0, "Dawaco": 0}

        # Questions and answers
        self.questions = [
            ("What drives you the most?",
             "Ambition and power", "Creativity and resilience", "Loyalty and honor", "Intelligence and cunning"),
            ("When faced with an obstacle, how do you react?",
             "Push through with sheer willpower", "Adapt and find an alternative way", "Stand firm and hold my ground", "Outsmart it using cleverness"),
            ("How do you handle responsibility?",
             "I take charge and lead", "I support and uplift others", "I stay loyal and committed", "I navigate it strategically"),
            ("Which of these is most important to you?",
             "Power and influence", "Creativity and expression", "Loyalty and duty", "Wit and charm"),
            ("If you could be any of these creatures, which would it be?",
             "A lion", "A rhinoceros", "An elephant", "A jackal"),
            ("How do you approach a difficult decision?",
             "With confidence and decisiveness", "By thinking outside the box", "By considering loyalty and duty", "By weighing all angles strategically"),
            ("What is your greatest strength?",
             "Determination and leadership", "Creativity and adaptability", "Bravery and dedication", "Sharpness and charm"),
            ("What kind of magic would you be most skilled at?",
             "Powerful enchantments", "Healing and creative spells", "Protective and defensive magic", "Illusions and trickery")
        ]

        self.current_question = 0
        self.colors = ["#FFC300", "#FF5733", "#33FF57", "#5733FF", "#FF33A6", "#33A6FF", "#A6FF33", "#FF9966"]

        # Show welcome screen first
        self.show_welcome_screen()

    def change_background(self):
        """Changes the background color to a random color from the list."""
        new_color = random.choice(self.colors)
        self.root.configure(bg=new_color)

    def show_welcome_screen(self):
        """Displays the welcome screen before starting the quiz."""
        self.clear_screen()
        self.change_background()

        welcome_text = (
            "Hello students,\n\n"
            "This small quiz will help you discover which House at "
            "Uagadou Academy of Magic is best suited for you!\n\n"
            "Simply answer 8 questions by selecting A, B, C, or D, and "
            "we'll reveal your true calling. Let's begin!"
        )

        label = tk.Label(self.root, text=welcome_text, wraplength=400, font=("Arial", 12), justify="center", bg=self.root["bg"])
        label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 14, "bold"), command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        """Starts the quiz by displaying the first question."""
        self.clear_screen()
        self.display_question()

    def display_question(self):
        """Display the current question and options."""
        self.clear_screen()
        self.change_background()
        
        question, *choices = self.questions[self.current_question]

        self.question_label = tk.Label(self.root, text=question, wraplength=400, font=("Arial", 14), justify="center", bg=self.root["bg"])
        self.question_label.pack(pady=20)

        self.options = []
        for i, choice in enumerate(choices):
            btn = tk.Button(self.root, text=choice, font=("Arial", 12), command=lambda idx=i: self.submit_answer(idx))
            btn.pack(fill="x", pady=5, padx=20)
            self.options.append(btn)

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 12), state="disabled", command=self.next_question)
        self.next_button.pack(pady=20)

    def submit_answer(self, idx):
        """Record the answer and enable the next button."""
        answers = ["Ingonyame", "Umkhombe", "Indlovu", "Dawaco"]
        selected_banner = answers[idx]
        self.scores[selected_banner] += 1
        self.next_button.config(state="normal")
        for btn in self.options:
            btn.config(state="disabled")

    def next_question(self):
        """Go to the next question or show the final result."""
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        """Calculate and display the final result."""
        highest_score = max(self.scores.values())
        banners = [banner for banner, score in self.scores.items() if score == highest_score]
        result = "Your banner is: " + ", ".join(banners)
        messagebox.showinfo("Quiz Result", result)
        self.root.destroy()

    def clear_screen(self):
        """Clears all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

# Create the application window
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
