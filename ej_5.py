class MaestroPizzero:  
 def __init__(self, nombre: str):  
    self.nombre = nombre  
  
 def tomarPedido(self):  
    print(f"{self.nombre} ha tomado el pedido.")  
  
 def cocinar(self):  
    print(f"{self.nombre} está cocinando la pizza.")  
  
 def entregar(self):  
    print(f"{self.nombre} ha entregado la pizza.")  
  
  
class Mozo:  
 def __init__(self, nombre: str):  
    self.nombre = nombre  
    self.pizzas = []  
  
 def tomarPizzas(self, pizzas):  
   self.pizzas = pizzas  
  
 def obtenerNombre(self):  
  return self.nombre  
  
 def servirPizzas(self):  
  for pizza in self.pizzas:  
    print(f"{self.nombre} está sirviendo la pizza {pizza.tipo}")  
  
  
class Pizza:  
    def __init__(self, tipo: str):  
        self.tipo = tipo  
  
  
class TesterPizzeria:  
 def main(self):  
    # 5.a Crear objetos MaestroPizzero, Mozo y Pizza  
    maestro = MaestroPizzero("Pipo")  # Un único maestro pizzero  
    mozo1 = Mozo("Marcos")
    mozo2 = Mozo("Lito")
    
    # Crear pizzas  
    pizza1 = Pizza("Común")  
    pizza2 = Pizza("Muzzarella")  
    
    # 5.b Enviar mensajes a MaestroPizzero  
    maestro.tomarPedido()  
    maestro.cocinar()  
    maestro.entregar()  
  
    # 5.c Enviar mensajes a los mozos para tomar y servir pizzas  
    mozo1.tomarPizzas([pizza1])  
    mozo2.tomarPizzas([pizza2])  
 

    print(f"{mozo1.obtenerNombre()} está sirviendo las pizzas:")  
    mozo1.servirPizzas()  
  
    print(f"{mozo2.obtenerNombre()} está sirviendo las pizzas:")  
    mozo2.servirPizzas()  
  
  
if __name__ == '__main__':  
    testerPizzeria = TesterPizzeria()  
    testerPizzeria.main()
