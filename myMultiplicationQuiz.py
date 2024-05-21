#prompt user with 10 multiplication questions, ranging from 0 x 0 to 9 x 9. without using pyinputplus
#If the user answers correctly, display "Correct!" for 1 second and move on to the next question.
#The user gets three tries to answer each question before the program moves on to the next question.
#Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.



import time, random

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    for i in range(3):
        try:
            answer = int(input(prompt))
        except ValueError:
            print('Please enter a number.')
            continue
        if answer == num1 * num2:
            print('Correct!')
            correctAnswers += 1
            break
        else:
            print('Incorrect. Try again.')
    time.sleep(8)  # Give the user a bit of time to answer the question.