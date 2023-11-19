from question import question

question_prompt= [
    "what colour is the wavelength 500nm? \n(a) orange\n(b) green\n(c) blue\n\n",
    "what is the nature of light? \n(a) Particle\n(b) wave\n(c) both\n\n",
    "what is the visible range of wavelength\n(a) 400-700nm\n(b) 400-900nm\n(c) 300-700nm\n\n"
]
question = [
    question(question_prompt[0], "b"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got "+str(score) + "/"+ str (len(questions))+" correct")

run_test(question)
