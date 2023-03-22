from app.mini_calulator import Mini_Calculator


class Test_Mini_Calc_Multiplication():

    def setup_method(self):
        self.calc = Mini_Calculator()

    def teardown_method(self):
        pass
        # aici se scriu instructiuni executate la final

    def test_multiplication(self):
        assert self.calc.multiplication(5, 4) == 20