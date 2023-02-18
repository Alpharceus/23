class Riemann:
    def __init__(self, a=0, b=1, int_type="left", int_func=lambda x: x):
        self.a = a
        self.b = b
        self.int_type = int_type
        self.int_func = int_func
        
    def do_int(self, n):
        dx = (self.b - self.a) / n
        result = 0
        
        for i in range(n):
            if self.int_type == "left":
                result += self.int_func(self.a + i*dx)
            elif self.int_type == "right":
                result += self.int_func(self.a + (i+1)*dx)
            elif self.int_type == "midpoint":
                result += self.int_func(self.a + (i+0.5)*dx)
                
        return result * dx
