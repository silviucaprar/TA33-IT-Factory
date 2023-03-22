"""
__ este prefixul pentru atributele private
nu trebuie folosita in afara clasei. Orice incercare de a face asta va rezulta intr-o eroare --> AttributeError
"""

class Car:
    def __init__(self, wheel, speed, color):
        self.__wheel = wheel  # private class atribute
        self.__speed = speed  # private class atribute
        self.__color = color  # private class atribute


renault = Car("right", 160, "red")
 # Cum se acceseaza? - REFRAIN FROM DOING SO!
print(renault._Car__speed)