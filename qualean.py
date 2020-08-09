from decimal import *

getcontext().prec = 10

class Qualean(object):

    def __init__(self,value):
        super().__init__()
        import random

        self.imaginary = Decimal(random.uniform(-1, 1))
        # print(getcontext().prec)
        self.value = Decimal(value)
        self.final_value = self.value*self.imaginary
        print(self.final_value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        if value not in [-1,-1.0,0,0.0,1,1.0]:
            raise ValueError("Value must be any of the values from [-1, 0, 1]")
        else:
            self.__value = value

    def __str__(self):
        return 'Qualean: real = {0}, imaginary = {1}'.format(self.__value, self.imaginary)

    def __repr__(self):
        return 'Qualean({0}, {1})'.format(self.__value, self.imaginary)

    def __and__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value > 0 and other.final_value)
        else:
            return NotImplemented    

    def __or__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value or other.final_value)
        else:
            return NotImplemented        

    def __add__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value + other.final_value)
        else:
            return NotImplemented
            
    def __eq__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value == other.final_value)
        else:
            return NotImplemented

    def __float__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value == other.final_value)
        else:
            return NotImplemented            

    def __ge__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value >= other.final_value)
        else:
            return NotImplemented   

    def __gt__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value > other.final_value)
        else:
            return NotImplemented   

    def __invertsign__(self):
        return (self.final_value * -1)
        
    def __le__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value <= other.final_value)
        else:
            return NotImplemented               

    def __lt__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value < other.final_value)
        else:
            return NotImplemented   

    def __mul__(self,other):
        if isinstance(other, Qualean):
            return (self.final_value * other.final_value)
        else:
            return NotImplemented   

    def __sqrt__(self):
        import math
        return math.sqrt(self.final_value)

    def __bool__(self):
        return (self.final_value > 0)
        