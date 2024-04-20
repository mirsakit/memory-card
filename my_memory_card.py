from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QButtonGroup,QWidget, QApplication, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QPushButton

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1  
        self.wrong2 = wrong2
        self.wrong3 = wrong3     

question_list =[]    
question_list.append(Question('В каком году началась Великая Отечественная война?', 'В 1941', 'В 1940', 'В 1939', 'В 1945'))    
question_list.append(Question('Кто был во главе 3 рейха?', 'Гитлер', 'Наполеон', 'Цезарь', 'Сталин'))    
question_list.append(Question('Какое сейчас время года?', 'Осень', 'Зима', 'Лето', 'Весна'))    
question_list.append(Question('Из какой страны шаурма?', 'Турция', 'Гемрания', 'Россия', 'США'))    
question_list.append(Question('Столица США?', 'Вашингтон', 'Москва', 'Берлин', 'Мехико'))    
question_list.append(Question('В какой стране столица Мехико?', 'Мексика', 'США', 'Великобритания', 'Португалия'))    
question_list.append(Question('Столица Великобритании?', 'Лондон', 'Уэльс', 'Бразилия', 'Что?')) 
question_list.append(Question('Кто открыл Америку?', 'Колумб', 'Ленин', 'Веспуччи', 'Вашингтон'))
question_list.append(Question('Столица Польши?', 'Варшава', 'Берлин', 'Лиссабон', 'Рига'))  
question_list.append(Question('Из какой страны BMW, Mercedes-benz и Audi?', 'Германия', 'Россия', 'Китай', 'США')) 

app = QApplication([])
main_win = QWidget()
main_win.resize(450, 300)
main_win.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить')
question = QLabel('В каком году началась Великая Отечественная война?')

RadioGroupBox = QGroupBox('варианты ответов:')
btn1 = QRadioButton('В 1940')
btn2 = QRadioButton('В 1945')
btn3 = QRadioButton('В 1939')
btn4 = QRadioButton('В 1941')
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn1)
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)
layout_ans3.addWidget(btn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет')
lb_correct = QLabel('Ответ будет тут')
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lb_correct, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_ans4)

layout_line = QVBoxLayout()
layout_line.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line.addWidget(btn_OK, stretch=2)
main_win.setLayout(layout_line)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Продолжить')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!!')
        main_win.score+=1
        print('Статистика\n Всего вопросов:', main_win.total, 'Количество верных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100, '%')    
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно!!')
            print('Рейтинг:', main_win.score/main_win.total*100, '%')    

def next_question():
    main_win.total+=1
    print('Статистика\n Всего вопросов:', main_win.total, 'Количество верных ответов:', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100, '%')    
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.score = 0

btn_OK.clicked.connect(click_OK)
next_question()

main_win.show()
app.exec_()