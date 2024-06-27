from data import question_data
from quiz_brain import QuizBrain


class Question:
    """
            Initialize the Question object with text and answer.

            Parameters:
            q_text (str): The text of the question.
            q_answer (str): The answer to the question (True/False).
            """
    def __init__(self, q_text, q_answer):
        self.q_text = text
        self.q_answer = answer


question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()
