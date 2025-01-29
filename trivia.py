import random
import time

class Question:
    """Represents a single quiz question."""
    def __init__(self, text, options, answer, hint):
        self.text = text
        self.options = options
        self.answer = answer
        self.hint = hint

    def ask(self):
        """Displays the question and checks the user's answer within a time limit."""
        print("\n" + self.text)
        for option in self.options:
            print(option)

        start_time = time.time()  # Start timer
        user_answer = input("\nYour answer (A, B, C, or D): ").strip().upper()

        if user_answer == "HINT":
            print(f"Hint: {self.hint}")
            user_answer = input("Your final answer: ").strip().upper()

        elapsed_time = time.time() - start_time  # Time taken

        if elapsed_time > 10:
            print("⏳ Time's up! You took too long to answer.")
            return 0  

        if user_answer == self.answer:
            print("✅ Correct!\n")
            return 1  
        else:
            print(f"❌ Wrong! The correct answer is {self.answer}\n")
            return 0  

class QuizGame:
    """Manages the quiz game."""
    def __init__(self, questions):
        self.questions = [Question(**q) for q in questions]
        random.shuffle(self.questions)
        self.score = 0

    def start(self):
        """Runs the quiz and tracks the score."""
        print("\n🎯 Welcome to the IQ Trivia Challenge! Type 'HINT' if you're stuck. You have **10 seconds** per question!")

        for i in range(min(3, len(self.questions))):  # Ask up to 3 unique questions
            self.score += self.questions[i].ask()

        print(f"\n🏆 Quiz Over! Your final score: {self.score}/3")
        if self.score == 3:
            print("🔥 Perfect! You're a genius!")
        elif self.score == 2:
            print("👏 Good job! Just one step away from perfection.")
        else:
            print("🤔 Keep practicing, you'll get better!")

# Question Bank
questions = [
    {"text": "What is the capital of France?", 
     "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
     "answer": "C",
     "hint": "It's known as the city of love."
    },
    {"text": "What is 7 + 8?", 
     "options": ["A) 13", "B) 15", "C) 14", "D) 16"],
     "answer": "B",
     "hint": "It's an odd number."
    },
    {"text": "Which planet is known as the Red Planet?", 
     "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
     "answer": "B",
     "hint": "It is named after the Roman god of war."
    }
]

# Start the quiz
quiz = QuizGame(questions)
quiz.start()
