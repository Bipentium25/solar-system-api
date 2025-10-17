class Planet:
    def __init__(self,id,name,description,has_flag):
        self.id = id
        self.name = name
        self.description = description
        self.has_flag = has_flag

planets = [
    Planet(1, "Mercury", "The smallest and innermost planet, very hot and rocky.", False),
    Planet(2, "Venus", "Second planet from the Sun, covered in thick toxic clouds.", False),
    Planet(3, "Earth", "Our home planet, the only known one with life.", True),
    Planet(4, "Mars", "The red planet, known for its iron oxide surface and potential for past water.", True),
    Planet(5, "Jupiter", "The largest planet, a gas giant with a prominent Great Red Spot.", False),
    Planet(6, "Saturn", "Gas giant famous for its stunning ring system.", False),
    Planet(7, "Uranus", "Ice giant with a blue-green color and tilted rotation axis.", False),
    Planet(8, "Neptune", "Ice giant farthest from the Sun, known for strong winds and storms.", False)
]