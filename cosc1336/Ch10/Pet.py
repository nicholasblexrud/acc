# a) Nick Blexrud 
# b) status = Complete 
# c) This class define the construct of a Pet and consists of the following data attributes: name, animal type and age.
# The Pet class provides getters and setters to access and modify the data attributes.
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age