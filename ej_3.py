class Mozo:  
  def __init__(self, nombre: str):  
     self.nombre = nombre  
     self.pizzas = []  # Lista vacía de pizzas  
  
  def establecerNombre(self, nombre: str):  
    self.nombre = nombre  
    return self.nombre
  
  def tomarPizzas(self, pizzas):  
    if not self.pizzas:  
     self.pizzas.extend(pizzas[:2])  
    else:  
     print("El mozo ya tiene el máximo de pizzas permitidas (2).")  
  
  def servirPizzas(self):  
    self.pizzas.clear()  
  
  def nombre(self):  
    return self._nombre  
  
  
  def pizzas(self):  
    return self._pizzas  
  
  def esta_libre(self):  
    return not self.pizzas
  
  print("Mozos\n")
mozo = Mozo("Marcos")
print(f"Se trata del mozo --> {mozo.establecerNombre("Marcos")}")

