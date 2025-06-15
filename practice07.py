#7. 🧠 **Mini Quiz Game (1-2 savol)**

# Vazifa: Savol beriladi, javobni tekshiradi.
# Funksiya: ask_question(question: str, correct_answer: str)`
# check_answer(user_answer, correct_answer)

def ask_question(question):
    user_answer = input(f"{question}").strip()
    return user_answer

def check_answer(user_answer,correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    return result

def main():
    question = "O'zbekistonning poytaxti qayer ?"
    correct_anwer = "Toshkent"
    
    user_answer = ask_question(question)
    is_correct = check_answer(user_answer,correct_anwer)
    
    if is_correct:
        print("tog'ri topdinggiz")
    else:
        print(f"topolmadinggiz,tog'ri javob \"{correct_anwer}\"")

main()
    


    
    
