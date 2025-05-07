from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Video(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    release_date: Mapped[str]
    total_inventory: Mapped[int]
    rentals: Mapped[list["Rental"]] = relationship(back_populates="video")

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            release_date=self.release_date,
            total_inventory=self.total_inventory,
        )
    
    def update(self, data):
        self.title = data["title"]
        self.release_date = data["release_date"]
        self.total_inventory = data["total_inventory"]

    def is_available(self):
        return self.get_available_count() > 0
    
    def get_available_count(self):
        rented_count = sum(rental.status == "RENTED" for rental in self.rentals)
        return self.total_inventory - rented_count

    @classmethod
    def from_dict(cls, data):
        return Video(
            title=data["title"],
            release_date=data["release_date"],
            total_inventory=data["total_inventory"],
        )