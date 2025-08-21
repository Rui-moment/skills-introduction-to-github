class Person(object):
    def __init__(self, age=1):
        self.age = age
    
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')
        
class Baby(Person):
    def __init__(self, age=1):
            if age < 18:
                super().__init__(age)
            else:
                raise ValueError('NO')
            
class Adult(Person):
    def __init__(self, age=18):
            if age >= 18:
                super().__init__(age)
            else:
                raise ValueError('NO')
baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()
        print('ride')

car = Car()
car.ride(adult)


class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run 
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')     

tesla_car = TeslaCar('Model S')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)


