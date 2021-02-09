"""This is object oriented programming"""


class BareMinimumClass:
        pass


class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

        def add(self, other_complex):
            """Adds complex numbers"""
            self.r += other_complex.r
            self.i += other_complex.i 
        def __repr__(self):
            return "({}, {}i)".format(self.r, self.i)


class SocialMediaUser:
        def __init__(self, name, location, upvotes=0):
                self.name = str(name)
                self.location = location
                self.upvotes = int(upvotes)

        def recieve_upvotes(self, num_upvotes=1):
                self.upvotes += num_upvotes
        
        
        def is_popular(self):
            return self.upvotes > 100


class Animal:
        """General Representation of Animals"""
        def __init__(self, name, weight, location="Earth", diet_type="Food", poisonous="False"):
            self.name = name
            self.weight = weight
            self.location = location
            self.diet_type = diet_type
            self.poisonous = poisonous
        
        def eat(self, food):
            return "Huge fan of that " + food

        def run(self):
            return "Vroom, Vroom, I go quick"

class Sloth(Animal):
        pass
