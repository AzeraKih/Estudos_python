##Define a class Circle with attribute radius.
##Also, define the following:
##    a class variable count, which determines the number of circles created
##    a method area that calculates the area of a circle.
##The input should be comma separated values.Output should be the area for each
##value and the total number of circles created.
##Check the main/tail section for output handling (read only)
##Use the 'Test against custom input' box below to output your result for
##debugging - Provide float values separated by comma (refer test case 
##samples below) to display the output / error.
##    The outputs are split in 2 lines
##    1st output provides area of circle for all the inputs provided
##    2nd output is the number of circles created or the number of
##    inputs provided. Testcase 1:Input.

##class Circle:
##    no_of_circles = 0
##
##    def area(self):
##        return 3.14 * (self.raio**2)
##    
##    def __init__(self, raio):
##        self.raio = raio
##        Circle.no_of_circles += 1
##
##
##raios = [float(i) for i in input("Digite os raios separado por ','").split(",")]
##circles = [Circle(i) for i in raios]
##
##print([i.area for i in circles])
##print(Circle.no_of_circles)


##Define a class method getCircleCount inside Circle such that it returns the number of created circle objects.
##	Hint: Use classmethod decorator.
##Try accessing the class method using a object and also the class.
##Provide the radius of each circle in the input to test the number of circles created along with the area of each circle.
##Output the total count of circles.
##	Check the main/tail section for output handling (read only)
##Use the 'Test against custom input' box below to output your result for debugging - Provide float values separated by comma (refer test case samples below) to display the output / error. The outputs are split in 2 lines
##	1st output provides a key value pair of circle number and it's corresponding area. 
##	2nd output is the number of circles created or the number of inputs provided.
##
##class Circle:
##    no_of_circles = 0
##
##    def area(self):
##        return 3.14 * (self.raio**2)
##    
##    def __init__(self, raio):
##        self.raio = raio
##        Circle.no_of_circles += 1
##        
##    @classmethod
##    def getCircleCount(Class):
##        return Circle.no_of_circles
##
##
##raios = [float(i) for i in input("Digite os raios separado por ','").split(",")]
##circles = [Circle(i) for i in raios]
##
##print([i.area() for i in circles])
##print(Circle.getCircleCount())


##Define a static method getPi inside Circle, which returns the value 3.14
##    Hint: Use staticmethod decorator.
##Redefine the area method such that it uses getPi static method in it.
##Try accessing the static method using a object and also the class.
##    Check the main/tail section for output handling (read only)
##Use the 'Test against custom input' box below to output your result
##for debugging - Provide float values separated by comma
##refer test case samples below) to display the output / error.
##the output provides a key value pair of circle number and it's
##corresponding area.


##class Circle:
##    no_of_circles = 0
##
##    def area(self):
##        return Circle.getPI() * (self.raio**2)
##    
##    def __init__(self, raio):
##        self.raio = raio
##        Circle.no_of_circles += 1
##        
##    @classmethod
##    def getCircleCount(Class):
##        return Circle.no_of_circles
##
##    @staticmethod
##    def getPI():
##        return 3.14
##
##
##raios = [float(i) for i in input("Digite os raios separado por ','").split(",")]
##circles = [Circle(i) for i in raios]
##
##print([i.area() for i in circles])
##print(Circle.getCircleCount())














































