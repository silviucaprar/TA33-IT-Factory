"""
Tipuri de constructori:
- explicit - definit de utilizator
- implicit - cand nu este definit de utilizator, se foloseste cel built-in
"""


class Mini_Calculator:

    def add_numbers(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b

    def multiplication(self,a, b):
        return a * b

    def division(self, a, b):
        return a / b
