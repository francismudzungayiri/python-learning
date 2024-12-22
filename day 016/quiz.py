from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for ques in question_data:
    question = Question(ques['text'], ques['answer'])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
    
    
    
        