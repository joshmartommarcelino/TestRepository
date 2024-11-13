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



score = 0

Question_1 = (input("1.What is the capital of France: "))
Question_1 = Question_1.lower()
if Question_1 == "paris":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_2 = (input("2.What is the capital of Norway: "))
Question_2 = Question_2.lower()
if Question_2 == "oslo":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_3 = (input("3.What is the capital of Switzerland: "))
Question_3 = Question_3.lower()
if Question_3 == "bern":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_4 = (input("4.What is the capital of Hungary: "))
Question_4 = Question_4.lower()
if Question_4 == "budapest":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_5 = (input("5.What is the capital of Greece: "))
Question_5 = Question_5.lower()
if Question_5 == "athens":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")
    
Question_6 = (input("6.What is the capital of Latvia: "))
Question_6 = Question_6.lower()
if Question_6 == "riga":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_7 = (input("7.What is the capital of Bulgaria: "))
Question_7 = Question_7.lower()
if Question_7 == "sofia":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_8 = (input("8.What is the capital of Spain: "))
Question_8 = Question_8.lower()
if Question_8 == "madrid":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_9 = (input("9.What is the capital of Poland: "))
Question_9 = Question_9.lower()
if Question_9 == "warsaw":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong")

Question_10 = (input("10.What is the capital of Sweden: "))
Question_10 = Question_10.lower()
if Question_10 == "stockholm":
      print("You are Correct")
      score = score + 1
else:
      print("You are Wrong") 
print(f"Quiz Completed! Your score is: {score}")
