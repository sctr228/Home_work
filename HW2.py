import random

# class Student:
#     amount_of_studens = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_studens += 1
#
# roman = Student()
# maria = Student(height=50)
# maria1 = Student(height=10)
# print(roman.height)
# print(maria.height)
# print(roman.amount_of_studens, 'Roman')
# print(Student.amount_of_studens, 'Students')


# class Student:
#     def __init__(self):
#         self.height += 10
#     height = 160
#     def printer(self):
#         print(self.height)
#
# roman = Student()
# roman1 = Student()
# roman2 = Student()
#
# roman.printer()


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 80
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 4
    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
    def to_chill(self):
        print('Rest time')
        self.gladness += 6
        self.progress -= 0.1
        self.money -= 8
    def to_work(self):
        print('Time to study')
        self.money += 8
        self.gladness -= 4
    def is_alive(self):
        if self.progress < - 0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <=0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed exernally...')
        elif self.money <=0:
            print('Bankrupt...')
    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Money = {self.money}')
    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

vasya = Student(name='Vasya')

for day in range(365):
    if vasya.alive == False:
        break
    vasya.live(day)