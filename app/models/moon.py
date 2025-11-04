from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    size: Mapped[int] 
    description:Mapped[str]
    has_flag: Mapped[bool]   
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id")) 
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "has_flag": self.has_flag,
            "planet": self.planet.name if self.planet_id else None
        }
    
    @classmethod
    def from_dict(cls, moon_data):
        # take dictionary
        # create moon
        # return moon
        return cls(name=moon_data["name"],
                    size=moon_data["size"],
                    description=moon_data["description"],
                    has_flag=moon_data["has_flag"],
                    planet_id=moon_data.get("planet_id", None)
        )