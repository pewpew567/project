class person:
    def __init__(self,name):
        self.name=name
    def setnumber(self,number):
        if(number<10000000000):
            self.number=number
    def setipaddres(self,ipaddres):
        if(ipaddres>0):
            self.ipaddres=ipaddres
    def getperson(self):
        print(self.name)
class student(person):
    id=1
    def __init__(self , tarikh):
        person().__init__(self, tarikh)
        self.tarikh=tarikh
    def setstatus(self,status=""):
        
        if(status=="freshman" or status=="sophomore" or status=="junior" or status=="senior"):
            self.status=status
    def getstatus(self):
        return self.status
    def gettarikh(self):
        print(self.tarikh)
    def printstudend(self):
        print(self.name + self.number + self.ipaddres +self.status + self.tarikh)
class epmploy(person):
    id=1
    def __init__(self,  numbere ,ipaddrese,tarikhe,salary ):
        self.tarikhe=tarikhe
        self.salary=salary
        person().__init__(self,numbere ,ipaddrese,tarikhe,salary)
    def gettarikh(self):
        print(self.tarikhe)
    def getsalary(self):
        print(self.salary)
    def printemploy(self):
        print( self. number + self.ipaddres +self.tarikhe + self.salary ) 
person1=person("meysam")
person1.setnumber(94534432213)
person1.setipaddres(1235564598)
person1.getperson()
student1=student("meysam",1399)
student1.setstatus("sophomore")
student1.printstudend()
epmploy1=epmploy(1399,18000000)
epmploy1.printemploy()




   
    

            
        
    

        
      