from abc import abstractmethod


    

class Musician:
    members = []
    def __init__(self, name):
        self.name=name
        Musician.members.append(self.name)
    @abstractmethod # Abstraction
    def __str__(self):
        pass
    @abstractmethod # Abstraction
    def __repr__(self):
        pass
    @abstractmethod # Abstraction
    def get_instrument(self):
        pass
    @abstractmethod # Abstraction
    def play_solo(self):
        pass

class Band(Musician):
    instances=[]
    def __init__(self, name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
             
    def play_solos(self):
        solos_list=[]
        for i in self.members:
            solos_list.append(i.play_solo())
        return solos_list
    def __str__(self):
        
        return f"We are {self.name} and we are music band"

    def __repr__(self):

        return f"Band instance. Name = {self.name}"
    @classmethod
    def to_list(cls):
        
        return cls.instances

        


    
    
    
class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return "bom bom buh bom"
    
    

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return "rattle boom crash"