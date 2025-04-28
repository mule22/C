import random
#1
def Shemtxveviti_Sia():
    lists = []

    for i in range(10):
        list_1 = []
    
        for j in range(3):
            random_number = random.randint(0, 100)  
            list_1.append(random_number)  
    
    
        lists.append(list_1)

    return lists

#2_3
class Tolferda_Trapezia:
    
    def __init__(self, b_h):
        self.base1 = b_h[0]
        self.base2 = b_h[1]
        self.height = b_h[2]

    
    def __str__(self):
        return ("ტოლფერდა ტრაფეცია:\n"
                "ფუძე_1: {}\n"
                "ფუძე_2: {}\n"
                "სიმაღლე: {}\n".format(self.base1, self.base2, self.height))

    
    def area(self):
        jami = self.base1 + self.base2
        area_value = (jami * self.height) / 2
        return area_value
    #4
    def __le__(self, other):
        if not isinstance(other, Tolferda_Trapezia):
            return NotImplemented
        
        return self.area() <= other.area()
 #5   
class Triangle(Tolferda_Trapezia):
    
    def __init__(self, dimensions):
        super().__init__([dimensions[0], 0, dimensions[1]])

     
    def __str__(self):
        return ("სამკუთხედი:\n"
                "ფუძე: {}\n"
                "სიმაღლე: {}\n".format(self.base1, self.height))

    
    def area(self):
        area_value = (self.base1 * self.height) / 2
        return area_value

#6
class Square(Triangle):
    
    def __init__(self, dimensions):
        super().__init__([dimensions[0], dimensions[0]])

    def __str__(self):
        return ("კვადრატი:\n"
                "სიგრძე: {}\n".format(self.base1))

    def area(self):
        area_value = pow(self.base1,2)
        return area_value

Shemtxveviti_Sia = Shemtxveviti_Sia()
dimensions_1 = random.choice(Shemtxveviti_Sia)
dimensions_2 = random.choice(Shemtxveviti_Sia)
trapecia_1 = Tolferda_Trapezia(dimensions_1)
trapecia_2 = Tolferda_Trapezia(dimensions_2)
print("ტრაფეცია_1:\n", trapecia_1)
print("ტრაფეცია_2:\n", trapecia_2)
print("ფართობი_1:", trapecia_1.area())
print("ფართობი_2:", trapecia_2.area())

if (trapecia_1 <= trapecia_2):
    print("ტრაფეცია_1_ის ფართობი ნაკლებია")
else:
    print("ტრაფეცია_1_ის ფართობი მეტია")

triangle_dimensions = random.choice(Shemtxveviti_Sia)[:2]
square_dimensions = random.choice(Shemtxveviti_Sia)[:1]
samkutxedi = Triangle(triangle_dimensions)
kvadrati = Square(square_dimensions)

print(samkutxedi)
print("სამკუთხედის ფართობი:", samkutxedi.area(), "\n")

print(kvadrati)
print("ფართობი:", kvadrati.area(), "\n")


