from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For session management

# Load questions from a JSON file
with open("questions.json", "r") as f:
    questions = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_quiz")
def start_quiz():
    session["score"] = 0
    session["questions"] = random.sample(questions, 3)  # Pick 3 unique questions
    session["current_index"] = 0
    return redirect(url_for("quiz"))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if session["current_index"] >= len(session["questions"]):
        return redirect(url_for("result"))

    question = session["questions"][session["current_index"]]

    if request.method == "POST":
        user_answer = request.form.get("answer")
        if user_answer == question["answer"]:
            session["score"] += 1
        session["current_index"] += 1
        return redirect(url_for("quiz"))

    return render_template("quiz.html", question=question, index=session["current_index"] + 1)

@app.route("/result")
def result():
    return render_template("result.html", score=session["score"])

if __name__ == "__main__":
    app.run(debug=True)
