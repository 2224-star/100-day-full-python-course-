#Create a program capable of displaying questions to the user like KBC.

# kBC style quiz program
# this program will ask the user a series of questions and check their answers.
# it will keep track of the score and display it at the end.

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Mahatma Gandhi", "D) Subhas Chandra Bose"],
        "answer": "A"
    }
]

score = 0

for idx, q in enumerate(questions, 1):
    print(f"Q{idx}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    if user_ans == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

print(f"Your final score: {score}/{len(questions)}")