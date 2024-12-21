class QuizBrain:
    
    def __init__(self, questions):
        self.q_number = 0
        self.ques_list = questions
        
    def next_question(self):
        current_question = self.ques_list[self.q_number]
        input(f'Q.{self.q_number + 1}: {current_question.question} (True /False).')