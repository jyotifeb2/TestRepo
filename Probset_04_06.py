from abc import ABC,abstractmethod
import math
class Temperature(ABC):
    @abstractmethod
    def __init__(self,temperature):
        pass
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def aboveFreeing(self):
        pass
    @abstractmethod
    def convertToFahren(self):
        pass
    @abstractmethod
    def convertToCelsius(self):
        pass
    @abstractmethod
    def convertToKelvin(self):
        pass
class Fahrenheit(Temperature):
    def __init__(self,temperature):
        self.temperature=temperature
    def __str__(self):
        return str(self.temperature)+' degrees Fahrenheit'
    def aboveFreeing(self):
        if self.temperature>32:
            return True
        else:
            return False
    def convertToCelsius(self):
        self.celcius=(self.temperature-32)*5/9
        return self.celcius
    def convertToKelvin(self):
        self.kelvin=(self.temperature-32)*5/9+273.14
        return self.kelvin
    def convertToFahren(self):
        pass
class Celsius(Temperature):
    def __init__(self,temperature):
        self.temperature=temperature
    def __str__(self):
        return str(self.temperature)+' degrees Celcius'
    def aboveFreeing(self):
        if self.temperature>0:
            return True
        else:
            return False
    def convertToFahren(self):
        self.farenheit=(self.temperature*9/5)+32
        return self.farenheit
    def convertToKelvin(self):
        self.kelvin=self.temperature+273.15
        return self.kelvin
    def convertToCelsius(self):
        pass
class Kelvin(Temperature):
    def __init__(self,temperature):
        self.temperature=temperature
    def __str__(self):
        return str(self.temperature)+' degrees Kelvin'
    def aboveFreeing(self):
        if self.temperature>273.15:
            return True
        else:
            return False
    def convertToFahren(self):
        self.farenheit=(self.temperature-273.15)*9/5+32
        return math.ceil(self.farenheit)
    def convertToCelsius(self):
        self.celcius=(self.temperature-273.15)
        return math.ceil(self.celcius)
    def convertToKelvin(self):
        pass
temp_farenheit=float(input("Enter the Farenheit Degrees : "))
temp_celcius=float(input("Enter the Celcius Degrees : "))
temp_kelvin=float(input("Enter the Kelvin Degrees : "))
farenheit=Fahrenheit(temp_farenheit)
celcius=Celsius(temp_celcius)
kelvin=Kelvin(temp_kelvin)
print('farenheit string : ',farenheit.__str__())
print('farenheit above freezing point : ',farenheit.aboveFreeing())
print('farenheit convert to celcius : ',farenheit.convertToCelsius())
print('farenheit convert to kelvin : ',farenheit.convertToKelvin())
print('celcius string : ',celcius.__str__())
print('celcius above freezing point : ',celcius.aboveFreeing())
print('celcius convert to farenheit : ',celcius.convertToFahren())
print('celcius convert to kelvin : ',celcius.convertToKelvin())
print('kelvin string : ',kelvin.__str__())
print('kelvin above freezing point : ',kelvin.aboveFreeing())
print('kelvin convert to farenheit : ',float(kelvin.convertToFahren()))
print('kelvin convert to celcius : ',float(kelvin.convertToCelsius()))