print("Clases V2 Maldonado Valentina")
# Zona de clase
class Datos:
    #El constructor funcion
    def __init__(self, estatura, peso):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} kg ")
    def mi_lista(self):
        chicles = ["Menta", "Hierba Buena", "Canela"]
        print(chicles)
        for chi in chicles:
            print("º", chi)
    def mi_tupla(self):
        aguasfrescas = ("Horchata", "Limon", "Tamarindo")
        print(aguasfrescas)
        for agu in aguasfrescas:
            print("º", agu)
    def mi_conjunto(self):
        pizza = {"De piña", "Con carne", "De queso"}
        print(pizza)
        for pi in pizza:
            print("º", pi)
    def mi_diccionario(self):
        comidastop = {
            "Top 1:" : "º Enchiladas Rojas",
            "Top 2:" : "º Sanwish",
            "Top 3:" : "º Ensalada de Atún"
        }
        print(comidastop)
        for o , i in comidastop.items():
            print(o,i)


# Creación de objeto info
info = Datos(1.62,72)

# Utilizando el obj. --> info
info.mostrar_datos()
print("Lista de sabores de Chicles / Maldonado Valentina")
info.mi_lista()
print("Tupla de sabores de Aguas Frescas / Maldonado Valentina")
info.mi_tupla()
print("Conjunto de Pizzas / Maldonado Valentina")
info.mi_conjunto()
print("Diccionario de Top comidas de Maldonado Valentina")
info.mi_diccionario()


