class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'I am {}, {} years old.' .format(self.name,self.age)

class NUSHPerson(Person):
    
    def __init__(self,name,age,matric):
        self.name = name
        self.age = age
        self.matric = matric
        self.gradyear = self.matric +5
    def retain(self):
        self.gradyear+=1
        return 'oh no! retention!'

    def graduation(self):
        return '{} will graduate in {}' .format(self.name,self.gradyear)

x = NUSHPerson('nicky',21,2007)

print x.graduation()
print x.retain()
print x.retain()
print x.retain()
print x.graduation()