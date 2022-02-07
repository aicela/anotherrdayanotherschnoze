#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())


@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)

@app.route("/profile1")
def profile1():
    return render_template("profile1.html")

@app.route("/anais")
def anais():
    return render_template("anais.html")

@app.route("/anna")
def anais():
    return render_template("anna.html")

@app.route("/aysela")
def anais():
    return render_template("aysela.html")


if __name__ == "__main__":
    app.run()
