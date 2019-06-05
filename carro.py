class Carro:
	def __init__(self,marca="",rodas = [],volante = "",motor =[],tanque=""):
		self.marca = marca
		self.volante = volante
		self.rodas = rodas 
		self.motor = motor 
		self.tanque = tanque 
	
	def getvolante(self):
		self.volante = volante
	def setvoltante(self,volante):
		return self.volante 

	def gettanque(self):
		self.tanque = tanque
	def settanque(self,tanque):
		return self.tanque

	def getmarca(self):
		self.marca = marca
	def setmarca(self,marca):
		return marca 

	def setrodas(self,rodas):
		return self.rodas
	def getrodas(self):
		self.rodas = rodas 

	def dicmotor(self):
		mot = {}
		mot[self.motor] = self.motor 
		return mot
a = Carro("Volvo",["11/12/2019","12/03/2019","17/08/2019","19/04/2019"],"Volvo","Fiat" "v8"," 100 10")

print(a.rodas)
print(a.marca)
print(a.tanque)
print(a.motor)
print(a.dicmotor())