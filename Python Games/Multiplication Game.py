import random

# Score track panna oru variable
score = 0
total_questions = 10

print("===== Multiplication Quiz Start! =====\n")

for i in range(1, total_questions + 1):
    # 1 to 20 range la rendu random numbers edukkurom
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Correct answer calculate pannurom
    correct_answer = num1 * num2

    # User kitta question kekkurom
    user_answer = input(f"Q{i}: {num1} x {num2} = ? ")

    # User answer ah number aa convert pannurom (text aa varum, so int() pannanum)
    try:
        user_answer = int(user_answer)
    except ValueError:
        user_answer = None  # Number illana, wrong ah maathidum

    # Answer check pannurom
    if user_answer == correct_answer:
        print("Correct! ✅\n")
        score += 1
    else:
        print(f"Wrong ❌. Correct answer: {correct_answer}\n")

# Final score kaatrom
print("===== Quiz Over! =====")
print(f"Your Score: {score} / {total_questions}")
