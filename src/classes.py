class Entity:
    def __init__(self, name, race, hp, entityclass, description, stats):
        self.name = name
        self.race = race
        self.hp = hp
        self.entityclass = entityclass
        self.abilities = []
        self.description = description
        self.stats = stats
        self.inventory = []
    
    
    def toString(self):
        return f"Entity name: {self.name}, race: {self.race}, hp: {self.hp} class: {self.entityclass}, abilities: {self.abilities}, description: {self.description}, stats: {self.stats}, inventory: {self.inventory} "
