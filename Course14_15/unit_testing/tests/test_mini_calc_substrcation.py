from app.mini_calulator import Mini_Calculator


class Test_Mini_Calc_Substraction():

    def setup_method(self):
        self.calc = Mini_Calculator()

    def teardown_method(self):
        pass
        # aici se scriu instructiuni executate la final

    def test_substraction(self):
        assert self.calc.substraction(20, 7) == 13