from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(name=planet_data["name"])
        return new_planet