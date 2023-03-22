from app.mini_calulator import Mini_Calculator


class Test_Mini_Calc_Adunare():

    def setup_method(self):
        # instructiuni de inceput
        self.calc = Mini_Calculator() # cream un obiect al clasei Mini_Calculator

    def teardown_method(self):
        pass
        # aici se scriu instructiuni executate la final

    def test_add_numbers(self):  # toate metodele de test trebuie sa inceapa cu test_
        assert self.calc.add_numbers(10, 15) == 25


