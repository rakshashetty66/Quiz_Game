print("--------------------------")
print("Welcome to My Quiz Game !!")

question_bank = [
    {"text": "The ability of one class to acquire methods and attributes of another class is called ____.",
     "answer": "A"},
    {"text": "Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "What is the depth of multilevel inheritance in Python?", "answer": "C"},
    {"text": "What does MRO stand for?", "answer": "B"},
    {"text": "Which type of inheritance is used when a class is derived from more than one base class?", "answer": "B"},
    {"text": "What keyword is used to inherit a class in Python?", "answer": "A"},
    {"text": "In Python, the default constructor is called ____.", "answer": "D"},
    {"text": "Which method is called automatically when an object is created in Python?", "answer": "A"},
    {
        "text": "What is the term for the ability of different objects to respond to the same method call in different ways?",
        "answer": "C"}
]

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
    ["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order",
     "D. Method Resolution Object"],
    ["A. Single inheritance", "B. Multiple inheritance", "C. Hybrid inheritance", "D. None of these"],
    ["A. Class", "B. Inheritance", "C. Polymorphism", "D. Abstraction"],
    ["A. Constructor", "B. Destructor", "C. Overloading", "D. Method"],
    ["A. __init__", "B. __del__", "C. __str__", "D. __repr__"],
    ["A. Polymorphism", "B. Encapsulation", "C. Inheritance", "D. Overloading"]
]

score = 0


def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer


for question_num in range(len(question_bank)):
    print("----------------------------------")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])

    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")

print(f"\nYour final score is: {score}/{len(question_bank)}")
