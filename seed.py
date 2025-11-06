
from app import create_app, db
from app.models.planet import Planet
from app.models.moon import Moon
from dotenv import load_dotenv

planets = [
    {
        "name": "Mercury",
        "description": "The smallest planet and closest to the Sun.",
        "moons": [
            {"name": "Caloris Minor", "size": 12, "description": "Tiny crater moon orbiting Mercury.", "has_flag": False},
        ],
    },
    {
        "name": "Venus",
        "description": "A hot planet with thick clouds of sulfuric acid.",
        "moons": [
            {"name": "Aphrodite I", "size": 23, "description": "Hypothetical volcanic moon.", "has_flag": False},
        ],
    },
    {
        "name": "Earth",
        "description": "The only planet known to harbor life and liquid water.",
        "moons": [
            {"name": "Moon", "size": 3474, "description": "Earth’s natural satellite that stabilizes its rotation.", "has_flag": True},
        ],
    },
    {
        "name": "Mars",
        "description": "A dusty red planet with canyons, volcanoes, and frozen poles.",
        "moons": [
            {"name": "Phobos", "size": 22, "description": "Inner moon, heavily cratered and doomed to crash into Mars.", "has_flag": False},
            {"name": "Deimos", "size": 12, "description": "Outer moon, small and smooth.", "has_flag": False},
        ],
    },
    {
        "name": "Jupiter",
        "description": "The gas giant with the Great Red Spot and dozens of moons.",
        "moons": [
            {"name": "Io", "size": 3643, "description": "Volcanically active moon with sulfurous plains.", "has_flag": False},
            {"name": "Europa", "size": 3121, "description": "Icy moon suspected to have a subsurface ocean.", "has_flag": False},
            {"name": "Ganymede", "size": 5268, "description": "The largest moon in the Solar System.", "has_flag": False},
        ],
    },
    {
        "name": "Saturn",
        "description": "Famous for its stunning rings, composed mostly of ice.",
        "moons": [
            {"name": "Titan", "size": 5150, "description": "Has thick atmosphere and liquid methane lakes.", "has_flag": False},
            {"name": "Enceladus", "size": 504, "description": "Icy moon that ejects water vapor from geysers.", "has_flag": False},
            {"name": "Mimas", "size": 396, "description": "Small cratered moon nicknamed the Death Star moon.", "has_flag": False},
        ],
    },
]

loaners = [
    {"name": "Orpheus", "size": 200, "description": "A wandering captured moon with mysterious origin.", "has_flag": False},
    {"name": "Echo", "size": 150, "description": "A rogue moon drifting between planetary orbits.", "has_flag": False},
    {"name": "Nyx", "size": 400, "description": "Dark moon with erratic orbit and unknown parent.", "has_flag": False},
]


def get_model_by_field(cls, data_dict, key_name):
    value = data_dict[key_name]
    stmt = db.select(cls).where(getattr(cls, key_name) == value)
    return db.session.scalar(stmt)


load_dotenv()
my_app = create_app()
with my_app.app_context():

    for planet_data in planets:
        planet = get_model_by_field(Planet, planet_data, "name")
        if not planet:
            planet = Planet(
                name=planet_data["name"],
                description=planet_data["description"]
            )
            db.session.add(planet)
            db.session.flush()  # get planet.id

    for moon_data in planet_data["moons"]:
        moon = get_model_by_field(Moon, moon_data, "name")
        if not moon:
            moon = Moon(
                name=moon_data["name"],
                size=moon_data["size"],
                description=moon_data["description"],
                has_flag=moon_data["has_flag"],
                planet_id=planet.id
            )
            db.session.add(moon)

    # Add loaner moons (no planet)
    for moon_data in loaners:
        moon = get_model_by_field(Moon, moon_data, "name")
        if not moon:
            moon = Moon(
                name=moon_data["name"],
                size=moon_data["size"],
                description=moon_data["description"],
                has_flag=moon_data["has_flag"],
                planet_id=None
            )
            db.session.add(moon)

    db.session.commit()
