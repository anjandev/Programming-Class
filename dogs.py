# Python program using classes.

class Dog:
    
    def __init__(self, name, age, color, yappiness):
        self.name = name
        self.age = age
        self.color = color
        self.yappiness = yappiness
        
    def __str__(self):
        return "A " + str(self.age) + " year old dog named " + self.name
    
    # Getters
    
    def get_yappy(self):
        for x in range(self.yappiness):
            print "Woof!"
    
dog1 = Dog("Rudolph", 4, "golden", 3)
dog2 = Dog("Charm", 7, "brown", 7)

print dog1
print dog2

dog = Dog()
dog.
