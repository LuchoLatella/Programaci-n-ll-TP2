class Pizza():
    def __init__(self,variedad):
        self.variedad = variedad

    def establecerVariedad(self, variedadPizza):
        self.variedad = variedadPizza

    def obtenerVariedad(self):
        return self.variedad
    
print("Pizzass\n")
pizza = Pizza("comun")
print(f"Variedad inicial --> {pizza.obtenerVariedad()}")
pizza.establecerVariedad("muzzarella")
print(f"Variedad final --> {pizza.obtenerVariedad()}")
