from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from .model_utilities import date_to_str
from datetime import datetime

class Customer(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    postal_code: Mapped[str]
    phone: Mapped[str]
    registered_at: Mapped[str]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            postal_code=self.postal_code,
            phone=self.phone,
            registered_at=self.registered_at,
        )

    def update(self, data):
        self.name = data["name"]
        self.postal_code = data["postal_code"]
        self.phone = data["phone"]
    
    @classmethod
    def from_dict(cls, data):
        return Customer(
            name=data["name"],
            postal_code=data["postal_code"],
            phone=data["phone"],
            registered_at=date_to_str(datetime.now()),
        )