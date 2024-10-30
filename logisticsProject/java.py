Web VPython 3.2

class Imaginary:
    def __init__(self, real, complex, power=1):
        self.real = real
        self.complex = complex
        self.power = power%4
        
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
        return f'{str(self.real)} + {str(self.complex)}i'
        
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

def subtract_complex(complex_list):
    new_list = []
    new_list.append(complex_list[0])
    for num in complex_list[1:]:
        num.set_real(num.get_real() * -1)
        num.set_imag(num.get_imag() * -1)
        new_list.append(num)
    return add_complex(new_list)
    
a = Imaginary(3, 4, 1)
b = Imaginary(7, 2, 6)
result = subtract_complex([a, b])
print(result.display())

