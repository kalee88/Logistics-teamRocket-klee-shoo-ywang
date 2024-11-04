Web VPython 3.2

class Imaginary:
    def __init__(self, real, complex, power=1):
        self.power = power%2
        if power%4==1:
            self.real = real
            self.complex = complex
        elif power%4==2:
            self.real = real-complex
            self.complex = 0
        elif power%4==3:
            self.real = real
            self.complex = -complex
        else:
            self.real = real+complex
            self.complex = 0
        
    def set_real(self, real):
        self.real = real
    
    def set_imag(self, complex):
        self.complex=complex
        
    def set_power(self, power):
        self.power = power%4
        
    def get_real(self):
        return self.real
    
    def get_imag(self):
        return self.complex
        
    def get_power(self):
        return self.power
        
    def display(self):
        operation_sign = '+' if self.complex >=0 else '-'
        return f'{str(self.real)} {operation_sign} {str(abs(self.complex))}i'
        
# Adds complex numbers
def add_complex(complex_list):
    real = 0
    complex = 0
    for num in complex_list:
        real += num.get_real()
        imag = num.get_imag()
        power = num.get_power()
        if power == 0:
            real += imag
        elif power == 1:
            complex += imag
        elif power == 2:
            real -= imag
        else:
            complex -= imag
    return Imaginary(real, complex)

# Subtracts complex numbers
def subtract_complex(complex_list):
    new_list = []
    new_list.append(complex_list[0])
    for num in complex_list[1:]:
        num.set_real(num.get_real() * -1)
        num.set_imag(num.get_imag() * -1)
        new_list.append(num)
    return add_complex(new_list)
    
# Multiply complex numbers
def mult_complex(complex_list):
    real1, complex1, p1 = complex_list[0].get_real(), complex_list[0].get_imag(), complex_list[0].get_power()
    
    for num in complex_list[1:]:
        real2, complex2, p2 = num.get_real(), num.get_imag(), num.get_power()
        bd = -(complex1 * complex2)
        new_real = real1 * real2 + bd
        ad = real1 * complex2
        bc = real2 * complex1
        new_imag = ad + bc
        
        real1, complex1, p1 = new_real, new_imag, 1
    return Imaginary(real1, complex1, p1)
    
a = Imaginary(3, 4, 1)
b = Imaginary(7, 2, 3)
c = Imaginary(8, 5, 9)
d = Imaginary(3, 8, 6)
e = Imaginary(6, 3, 2)
result = mult_complex([a, b, c, d, e])
print(result.display())
