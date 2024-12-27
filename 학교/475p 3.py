class Integer:
    def __init__ (self, value):
        self.value = value
    def __add__ (self, other):
        return self.value + other.value
    def __sub__ (self, other):
        return self.value - other.value
    
a = Integer(5)
b = Integer(3)


        
