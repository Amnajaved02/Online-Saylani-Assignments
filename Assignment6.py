
#Question1
#Object-oriented programming is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields, and code, in the form of procedures. A feature of objects is an object's procedures that can access and often modify the data fields of the object with which they are associated.

#Question 2
#It provides a clear modular structure for programs which makes it good for defining abstract datatypes in which implementation details are hidden
#Objects can also be reused within an across applications. The reuse of software also lowers the cost of development. More effort is put into the object-oriented analysis and design, which lowers the overall cost of development.
#It makes software easier to maintain. Since the design is modular, part of the system can be updated in case of issues without a need to make large-scale changes
#Reuse also enables faster development. Object-oriented programming languages come with rich libraries of objects, and code developed during projects is also reusable in future projects.
#It provides a good framework for code libraries where the supplied software components can be easily adapted and modified by the programmer. This is particularly useful for developing graphical user interfaces.
#Better Productivity as OOP techniques enforce rules on a programmer that, in the long run, help her get more work done; finished programs work better, have more features and are easier to read and maintain.

#Question 3

#A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

#A method is a piece of code that is called by a name that is associated with an object. In most respects it is identical to a function except for two key differences:
#A method is implicitly passed the object on which it was called.
#A method is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).

#Question 4 

#Class:
#It is a user defined data type, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class.

#Object:
#In object-oriented programming (OOP), objects are the things you think about first in designing a program and they are also the units of code that are eventually derived from the process. Each object is an instance of a particular class or subclass with the class's own methods or procedures and data variables.

#Attribute:
#In Object-oriented programming(OOP), classes and objects have attributes. Attributes are data stored inside a class or instance and represent the state or quality of the class or instance. In short, attributes store information about the instance.

#Behaviour:
#The behavior of an object is defined by its methods, which are the functions and subroutines defined within the object class. Without class methods, a class would simply be a structure. Methods determine what type of functionality a class has, how it modifies its data, and its overall behavior.

#Question 5
class Car :
  def _init_(self,make,color,name,engine,types): 
    self.make=make 
    self.color= color 
    self.name=name 
    self.engine=engine
    self.types=types 
  
  def print_Make(self):
    print("The make of the car is:",self.make)

  def print_Color(self):
    print("The color of the car is:",self.color)

  def print_Name(self):
    print("The name of the car is:",self.name)

obj1=Car("Honda", "BLue", "Civic", "2400cc","Automatic")
obj2=Car("Honda", "Red", "City", "3000cc","Automatic")
obj3=Car("Suzuki", "White", "Civic", "700cc","Manual")
obj4=Car("Faw", "Silver", "V2", "1800cc","Manual")
obj5=Car("Suzuki", "Grey", "Swift", "1200cc","Automatic")
obj1.print_Color()
obj2.print_Make()
obj3.print_Name()
obj4.print_Make()
obj5.print_Name()
