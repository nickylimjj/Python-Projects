class Person(object):
    Population = 0  #class variable
    def __init__(self,name,age):
        self.name = name    #instance variable
        self.age = age      #instance variable
        Person.Population +=1

    def __repr__(self):
        return 'I am {},aged {}' .format(self.name,self.age)

    def __del__(self):
        print "{} has died" .format(self.name)
        Person.Population -=1

    def eat(self,food):
        return 'I am eating {} slowly! :)' .format(food)
    

class Military(Person):
    def __init__(self,name,age,rank):
        Person.__init__(self,name,age)  #inheriting initialization of base class
        self.rank = rank

    def __repr__(self):
        return 'I am {} {},aged {}' .format(self.rank,self.name,self.age)
    
    def eat_during_training(self,food):
        return 'no time for {}! Charge that knoll!'.format(food)

    def eat_during_nontraining(self,food):  #calling method from base class
            return super(Military,self).eat(food)



nicky = Military('nicky',21,'LTA')
print nicky
print nicky.eat_during_training('chicken')
print nicky.eat_during_nontraining('beef')
print "Current population:", Person.Population
del(nicky)
print "Current population:", Person.Population