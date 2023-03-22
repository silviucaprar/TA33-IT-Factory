"""
protected members - sunt accesibili in interiorul clasei cat si in subclase.
- nu pot fi accesati din orice alta parte
instance variable protected --? _var_name (single underscore)
folosind unserscore, previne sa fie accesat, mai putin daca este accesat dintr-o subclasa
ca sa afisam, modifica si sterge o valoare, folosim getter, setter si deleter
"""


class Car:
    def __init__(self, wheel, speed, color):
        self._wheel = wheel  # protected class atribute
        self._speed = speed  # protected class atribute
        self._color = color  # protected class atribute

# we use decorator property
# ce cream aici va fi considerat o proprietate

    @property
    def car_wheel(self):
        pass

    @property
    def car_speed(self):
        pass

    @property
    def car_color(self):
        pass

# cream getterul folosindu-ne de getter decorator
# syntax: function_name(the one declared as property).getter

    @car_wheel.getter
    def car_wheel(self):
        print("Returning the wheel ... ")
        return self._wheel

    @car_color.getter
    def car_color(self):
        print("Returning the color ...")
        return self._color

    @car_speed.getter
    def car_speed(self):
        print("Returning the speed ...")
        return self._speed

# cream setterul folosindu-ne de getter decorator
# syntax: function_name(the one declared as property).setter

    @car_color.setter
    def car_color(self, new_color):
        print("Updating the car color...")
        self._color = new_color

    @car_speed.setter
    def car_speed(self, new_speed):
        print("Updating the car speed...")
        self._speed = new_speed

    @car_wheel.setter
    def car_wheel(self, new_wheel):
        print("Updating the car wheel...")
        self._wheel = new_wheel

# cream deleterul folosindu-ne de getter decorator
# syntax: function_name(the one declared as property).deleter

    @car_color.deleter
    def car_color(self):
        print(f"{self._color} was deleted.")
        self._color = None

    @car_speed.deleter
    def car_speed(self):
        print(f"{self._speed} was deleted.")
        self._speed = None

    @car_wheel.deleter
    def car_wheel(self):
        print(f"{self._wheel} was deleted.")
        self._wheel = None


peugeot = Car("right", 180, "white")
mitsubishi = Car("left", 200, "green")
# print(peugeot.color)  # if we write this way we get Attribute Error
# AttributeError: 'Car' object has no attribute 'color'. Did you mean: '_color'?

# get the color of peugeot and mitsubishi
# ne folosim de getter
print("Peugeot", peugeot.car_color)
print("Mitsubishi", mitsubishi.car_color)
print("\n")

# update the colors for peugeot and mitsubishi
# ne folosim de setter
peugeot.car_color = "black"
print("Peugeot", peugeot.car_color)
mitsubishi.car_color = "red"
print("Mitsubishi", mitsubishi.car_color)
print("\n")

# delete the color for mitsubishi and peugeot
# ne folosim de deletter
del peugeot.car_color
print("Peugeot", peugeot.car_color)
del mitsubishi.car_color
print("Mitsubishi", mitsubishi.car_color)



