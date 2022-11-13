#Напишите класс Python, который имеет два метода get_String и print_String. 
#get_String принимает строку от пользователя, 
#а print_String печатает строку в верхнем регистре.


class registr():
    def __init__(self):
        self.string = str
        
    def get_string(self):
        self.string = input()
        
    def print_string(self):
        print(self.string.upper())

f = registr()
f.get_string()
f.print_string()

    