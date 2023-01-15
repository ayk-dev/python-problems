class QuizBrain:
    def __init__(self, ql: list):
        self.question_number = 0
        self.questions_list = ql
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        user_answer = input(f'Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)?: ')
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user, correct):
        if user.lower() == correct.lower() or user.lower() in correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f'The correct answer is {correct}.')
        print(f'Your current score is: {self.score}/{len(self.questions_list)}.')
        print()
