# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
        self.type_coefficients = {
            'land': 0.85,
            'building site': 9,
            'forrest': 0.35
        }

    def calculate_tax(self):
        return math.ceil(self.area * self.type_coefficients[self.estate_type] * self.locality.coefficient)

    def __str__(self):
        tax = self.calculate_tax()
        return f"Zemědělský pozemek, lokalita {self.locality.name} (koeficient {self.locality.coefficient}), {self.area} metrů čtverečních, daň {tax} Kč"

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = math.ceil(self.area * self.locality.coefficient * 15)
        if self.commercial:
            tax *= 2
        return math.ceil(tax)

    def __str__(self):
        tax = self.calculate_tax()
        return f"Byt, lokalita {self.locality.name} (koeficient {self.locality.coefficient}), {self.area} metrů čtverečních, daň {tax} Kč"

# Testování
manetin = Locality('Manětín', 0.8)
brno = Locality('Brno', 3)

estate1 = Estate(manetin, 'land', 900)
print(estate1)

residence1 = Residence(manetin, 120, False)
print(residence1)

residence2 = Residence(brno, 90, True)
print(residence2)
