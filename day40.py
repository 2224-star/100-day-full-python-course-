

### Kon Banega Crorpati Game

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Nation?",
        "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Sardar Patel", "D. Bhagat Singh"],
        "answer": "B"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["A. HTML", "B. C++", "C. Python", "D. Java"],
        "answer": "A"
    },
    {
        "question": "Whch river is the longest in India?",
        "options":["A. Yamuna", "B. Ganga", "C. Bramaputra", "D. Godavari"],
        "answer": "B"
    },
    {
    "question": "Who wrote the national anthem of India?",
    "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
    "answer": "A"
},
{
    "question": "Which is the smallest state in India by area?",
    "options": ["A. Goa", "B. Sikkim", "C. Tripura", "D. Manipur"],
    "answer": "A"
},
{
    "question": "What is the chemical symbol for water?",
    "options": ["A. O2", "B. CO2", "C. H2O", "D. NaCl"],
    "answer": "C"
},
{
    "question": "Who invented the telephone?",
    "options": ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. Isaac Newton"],
    "answer": "B"
}
]

prize_money = [1000, 5000, 10000, 50000 , 600000, 1000000, 50000000, 60000000, 70000000]
total = 0

for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        total += prize_money[i]
        print(f"Correct! You have won ₹{total}")
    else:
        print("Wrong answer! Game over.")
        break

print(f"\nYou won a total of ₹{total}")