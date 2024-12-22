class QuizBrain:
    
    def __init__(self, questions):
        self.q_number = 0
        self.score = 0
        self.ques_list = questions
        
    def next_question(self):
        current_question = self.ques_list[self.q_number]
        user_answer = input(f'Q.{self.q_number+1}: {current_question.question} (True /False).')
        self.q_number += 1
        
        self.check_answer(user_answer, current_question.q_answer)
        
    def still_has_question(self):
        return self.q_number < len(self.ques_list)-1
    
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() ==  correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print('You got it wrong')
            
        print(f'Your score is {self.score} / {self.q_number}')
        
        