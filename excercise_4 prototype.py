def quiz():
    questions = {
        "1. What is the capital of France? ": "Paris",
        "2. What is the capital of Germany? ": "Berlin",
        "3. What is the capital of Italy? ": "Rome",
        "4. What is the capital of Spain? ": "Madrid",
        "5. What is the capital of Portugal? ": "Lisbon",
        "6. What is the capital of Sweden? ": "Stockholm",
        "7. What is the capital of Norway? ": "Oslo",
        "8. What is the capital of Denmark? ": "Copenhagen",
        "9. What is the capital of Finland? ": "Helsinki",
        "10. What is the capital of Greece? ": "Athens"
    }

    score = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", answer)

    print("Your final score is:", score, "out of 10")

quiz()