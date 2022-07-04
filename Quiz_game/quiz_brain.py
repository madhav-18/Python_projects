class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

        # TODO 2: checking if the answer was right
    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_answer}")

    # TODO 1: asking the questions
    def next_question(self):
        while self.still_has_question():
            current_question = self.question_list[self.question_number]
            """this line indicates in short(current_question.text)"""
            """current_question = self.question_list[0]................................................................
            the above line will display the value that is in the list at 0 """
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")
            self.check_answer(user_answer, current_question.answer)
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")




# TODO 3: checking if we're at the end of the quiz
