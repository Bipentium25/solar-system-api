from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description
            }
        
    @classmethod
    def from_dict(cls, planet_data):
        # take dictionary
        # create planet
        # return planet
        return cls(name=planet_data["name"],
                    description=planet_data["description"]
        )