# Write a program to Create quiz application.
def run_quiz():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pt", "B. .pyt", "C. .py", "D. .pyw"],
            "answer": "C"
        },
        {
            "question": "Which data type is used to store True or False values?",
            "options": ["A. Integer", "B. String", "C. Boolean", "D. Float"],
            "answer": "C"
        },
        {
            "question": "How do you start a for loop in Python?",
            "options": ["A. for x in y:", "B. for x to y:", "C. for each x in y", "D. loop x in y:"],
            "answer": "A"
        }
    ]
    
    score =0
    total_questions = len(questions)
    
    print("Welcome to the Python Quiz Application!")
    print("---------------------------------------")
    
    for i in range(total_questions):
        print(f"\nQuestion {i+1}: {questions[i]['question']}")
        for option in questions[i]['options']:
            print(option)       
        user_answer = input("\nEnter your answer (A, B, C, or D): ").upper()
        
        if user_answer == questions[i]['answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was {questions[i]['answer']}.")
            
    print("\n---------------------------------------")
    print("Quiz Completed!")
    print(f"Your final score is:- {score}/{total_questions}") 
    percentage = (score / total_questions) * 100
    print(f"Percentage scored:- {percentage}%")

run_quiz()
