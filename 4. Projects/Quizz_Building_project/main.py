from question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b)Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n\n",
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'b')
]


def run_quizz(ques):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {score}/{len(questions)} correct!')


run_quizz(questions)
