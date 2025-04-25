class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self) -> str:
        return f"persona(nombre='{self.nombre}', edad={self.edad})"

    def __eq__(self, otra_persona) -> bool:
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.age

    def __lt__(self, otra_persona) -> bool:
        return self.edad < otra_persona.edad

    def __add__(self, otra_persona):
        return self.edad + otra_persona.edad


p1 = Persona("Persona", 38)
p2 = Persona("Entrometida", 27)
p3 = Persona("Va pa fuera", 25)

print(p1)
