class QuizBrain:
    """
            Initialize the QuizBrain with a list of questions.

            Parameters:
            q_list (list): List of Question objects.
            """
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.points = 0

    def next_question(self):
        """
                Ask the next question in the quiz.

                Continues until all questions are asked, then prints the final score.
                """
        while True:
            if self.q_number < len(self.q_list):
                current_question = self.q_list[self.q_number]
                print(f"Q.{self.q_number + 1} {current_question.q_text} (True/False)")
                user_input = input("")
                if user_input == current_question.q_answer:
                    self.points += 1
                self.q_number += 1

            else:
                print(f"You have completed the quiz.Your final score is {self.points}")
                return False
