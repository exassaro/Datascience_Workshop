class Person:
    species = "Homo sapiens"
    
    def __init__(self, name):
        self.name = name

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

# Usage
print(Person.species)  # Output: Homo sapiens
Person.set_species("Human")  # Change the class-level attribute
print(Person.species)  # Output: Human
