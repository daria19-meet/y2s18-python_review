class SuperHeros:
    def __init__(self, name, superpower, strength):
        self.name=name
        self.superpower=superpower
        self.strength=strength
    
    def x(self):
        print(self.name, self.superpower)
    
    def save(self, work):
        self.strength=self.strength-work
        if self.strength>0:
            print("Now your superhero has", self.strength,"energy")
        else:
            print("Your superhero doesnt have power left!")
        

s=SuperHeros("Superman", "Strength", 10)
s.x()
s.save(10)