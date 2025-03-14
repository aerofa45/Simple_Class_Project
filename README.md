# The explanation is done through assistance of AI since it seemed redundant for me to do it:

## **1. Overview**  
This program creates a **quiz game** using the `tkinter` module in Python.  
- The quiz helps users determine which **house** at Uagadou Academy of Magic suits them best.  
- Users answer **8 multiple-choice questions**.  
- Based on their responses, the program assigns them one of **four houses**:  
  - **Ingonyame**  
  - **Umkhombe**  
  - **Indlovu**  
  - **Dawaco**  
- The final result is displayed in a **popup window** using `messagebox`.

---

## **2. Breaking Down the Code**
### **(A) Importing Required Libraries**
```python
import tkinter as tk
from tkinter import messagebox
import random
```
- `tkinter`: Used to create the GUI (Graphical User Interface).  
- `messagebox`: Used to show pop-up messages.  
- `random`: Used to change background colors randomly.

---

### **(B) Class `QuizGame` (Main Class)**
```python
class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("2025 Quiz of Uagadou Academy of Magic")
        self.root.geometry("500x400")
```
- The **class `QuizGame`** contains all the logic for the quiz.  
- `__init__` (Constructor) initializes the game window and settings.

--- # Please understand the use of class, tuple, list and constructor if you want to understand the basic of this program, the main core of this program or logic is this:

class QuizGame:
    def __init__(self, root):  # Constructor
        self.root = root  # Window
        self.root.title("Quiz Game")  # Set window title
        
        self.scores = {"Ingonyame": 0, "Umkhombe": 0, "Indlovu": 0, "Dawaco": 0}  # Score dictionary
        
        self.questions = [  # List of questions
            ("What drives you the most?", "Ambition", "Creativity", "Loyalty", "Intelligence"),
            ("How do you handle responsibility?", "Take charge", "Support others", "Stay loyal", "Strategize"),
        ]

        self.current_question = 0  # Question counter
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))  # Display question
        self.question_label.pack(pady=20)

        self.options = []  # Create answer buttons
        for i in range(4):
            btn = tk.Button(root, text="", command=lambda idx=i: self.submit_answer(idx))
            btn.pack()
            self.options.append(btn)

        self.next_button = tk.Button(root, text="Next", state="disabled", command=self.next_question)
        self.next_button.pack(pady=20)

        self.display_question()  # Call function to show the first question

# If you understand what I wrote above like classes and constructors, others code is simple logic like using for in lists, and understanding the tkinter library. You can read about library in: https://docs.python.org/3/library/tkinter.html 

### **(C) Initialize Scores and Questions**
```python
# Initialize scores
self.scores = {"Ingonyame": 0, "Umkhombe": 0, "Indlovu": 0, "Dawaco": 0}

# Questions and answers
self.questions = [
    ("What drives you the most?",
     "Ambition and power", "Creativity and resilience", "Loyalty and honor", "Intelligence and cunning"),
    ("When faced with an obstacle, how do you react?",
     "Push through with sheer willpower", "Adapt and find an alternative way", "Stand firm and hold my ground", "Outsmart it using cleverness"),
    ...
]
```
- `self.scores`: Stores points for each house.  
- `self.questions`: Stores a list of questions with **4 answer choices**.  

---

### **(D) Track Question Number & Colors**
```python
self.current_question = 0
self.colors = ["#FFC300", "#FF5733", "#33FF57", "#5733FF", "#FF33A6", "#33A6FF", "#A6FF33", "#FF9966"]
```
- `self.current_question`: Keeps track of the current question.  
- `self.colors`: A list of **random background colors** to change the look of the quiz.

---

### **(E) Show Welcome Screen**
```python
self.show_welcome_screen()
```
- Calls the `show_welcome_screen()` function to **display a welcome message** before starting the quiz.

---

## **3. Core Functions**
### **(A) Changing Background Color**
```python
def change_background(self):
    new_color = random.choice(self.colors)
    self.root.configure(bg=new_color)
```
- Selects a **random color** from `self.colors` and sets it as the **background**.

---

### **(B) Welcome Screen**
```python
def show_welcome_screen(self):
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
```
- **Clears the screen** and changes the background.  
- **Displays the welcome text** in a `Label`.  
- **Creates a "Start Quiz" button** that calls `start_quiz()`.

---

### **(C) Starting the Quiz**
```python
def start_quiz(self):
    self.clear_screen()
    self.display_question()
```
- **Clears the welcome screen**.  
- Calls `display_question()` to show the **first question**.

---

### **(D) Displaying Questions**
```python
def display_question(self):
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
```
- **Displays the question and answer choices**.  
- **Creates 4 answer buttons**, each calling `submit_answer(idx)`.  
- **Next button starts as "disabled"** and is only enabled after selecting an answer.

---

### **(E) Submitting an Answer**
```python
def submit_answer(self, idx):
    answers = ["Ingonyame", "Umkhombe", "Indlovu", "Dawaco"]
    selected_banner = answers[idx]
    self.scores[selected_banner] += 1
    self.next_button.config(state="normal")
    for btn in self.options:
        btn.config(state="disabled")
```
- Updates the score of the **selected house**.  
- Enables the **Next button**.  
- Disables **other answer buttons**.

---

### **(F) Moving to Next Question**
```python
def next_question(self):
    self.current_question += 1
    if self.current_question < len(self.questions):
        self.display_question()
    else:
        self.show_result()
```
- Moves to the **next question**.  
- If **all questions are answered**, calls `show_result()`.

---

### **(G) Showing Final Result**
```python
def show_result(self):
    highest_score = max(self.scores.values())
    banners = [banner for banner, score in self.scores.items() if score == highest_score]
    result = "Your banner is: " + ", ".join(banners)
    messagebox.showinfo("Quiz Result", result)
    self.root.destroy()
```
- Finds the **house with the highest score**.  
- Displays the **result in a popup window**.  
- Closes the program.

---

### **(H) Clearing the Screen**
```python
def clear_screen(self):
    for widget in self.root.winfo_children():
        widget.destroy()
```
- **Removes all widgets** (text, buttons) before displaying new content.

---

## **4. Running the Program**
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
```
- Creates a **Tkinter window**.  
- Starts the **QuizGame class**.  
- Runs `root.mainloop()` to **keep the app running**.

---

## **5. Summary**
 **Uses Tkinter** to create a **graphical quiz**.  
 **Randomizes background colors** for an interactive look.  
 **Stores scores** for 4 houses and calculates the best match.  
 **Uses functions for modularity** (e.g., `clear_screen()`, `submit_answer()`).  
 **Displays results** using `messagebox`.  

Let me know if you have any questions! 🚀
