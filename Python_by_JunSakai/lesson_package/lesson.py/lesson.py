class Person(object):
    def __init__(self, name):
        self.name = name
    
    def say_somthing(self):
        print('I am {}.'.format(self.name))
        self.run(10)

    def run(self, num):
        print('I am running!' * num)

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_somthing()

del person

print('########')

