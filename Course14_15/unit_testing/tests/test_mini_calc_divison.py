from app.mini_calulator import Mini_Calculator


class Test_Mini_Calc_Division():

    def setup_method(self):
        self.calc = Mini_Calculator()

    def teardown_method(self):
        pass
        # aici se scriu instructiuni executate la final

    def test_division(self):
        rezultat = self.calc.division(6, 2)
        assert rezultat == 3