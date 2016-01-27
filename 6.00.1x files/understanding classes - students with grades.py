class student(object):
        nextIDnum = 1  #class attribute. called with student.nextIDnum
        
        #self used to indicate entering of that instance/frame
        
        def __init__(self,name):
            self.name=name
            self.grades=[]
            self.ID = student.nextIDnum
            student.nextIDnum +=1
            
        def addGrade(self,grade):
            self.grades.append(int(grade))
            
        def getGrades(self):
            return self.grades
        def getAverage(self):
            self.avg = round(sum(self.grades)/float(len(self.grades)),0)
            return 'my average is {}'.format(self.avg)
            
        def __str__(self):
            return 'my name is {}! \nmy school ID num is:{}.\nmy grades are as follows: \n{}'.format(self.name,self.ID,self.grades)

s1 = student('shaun')
s1.addGrade(80)
s1.addGrade(92)
s1.addGrade(70)

s2 = student('tuck leong')
s2.addGrade(68)
s2.addGrade(23)
s2.addGrade(100)

print s1
print s1.getAverage()
print ''
print s2
print s2.getAverage()


#wrapper function that allows you to key in grades fast for a student

def keygrades(name,grade):
    '''
    name: a string
    grade: a string in this format. "91 92 12 50"
    '''
    s1 = student(name)
    for i in grade.split(' '):
        s1.addGrade(i)
    print s1
    print s1.getAverage()