from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from datetime import datetime, timedelta

class Rental(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    video_id: Mapped[int] = mapped_column(ForeignKey("video.id"))
    due_date: Mapped[str]
    status: Mapped[str]  # RENTED or AVAILABLE
    customer: Mapped["Customer"] = relationship(back_populates="rentals")
    video: Mapped["Video"] = relationship(back_populates="rentals")

    def to_dict(self):
        return dict(
            customer_id=self.customer_id,
            video_id=self.video_id,
            due_date=self.due_date,
            # videos_checked_out_count=self.postal_code,
            available_inventory=self.video.get_available_count(),
        )

    @classmethod
    def from_dict(cls, data):
        return Rental(
            customer_id=data["customer_id"],
            video_id=data["video_id"],
            due_date=cls.calculate_due_date(),
            status="RENTED",
        )
    
    @classmethod
    def calculate_due_date(cls):
        return datetime.now() + timedelta(days=7)