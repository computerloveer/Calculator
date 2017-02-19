#!/usr/bin/python

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Sum(self):
        return self.a + self.b

    def Subtraction(self):
        return self.a - self.b

    def Beat(self):
        return self.a * self.b

    def Division(self):
        return self.a / self.b


a = raw_input("Enter the number one : ")
b = raw_input("Enter the number two : ")
practice = raw_input("Enter the practice in number : ")
MyCalc = calculator(int(a), int(b))

if practice == "sum":
    print MyCalc.Sum()
elif practice == "subtraction":
    print MyCalc.Subtraction()
elif practice == "beat":
    print MyCalc.Beat()
elif practice == "division":
    print MyCalc.Division()
