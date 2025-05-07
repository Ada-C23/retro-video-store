from app.models.customer import Customer
from app.models.model_utilities import date_to_str
from datetime import datetime, timedelta
import random

from app.db import db

def load():
    first_names = [
        "Jaime",
        "Grant",
        "Loren",
        "Domingo",
        "Peggy",
        "Tyler",
        "Grady",
        "Brenda",
        "Wilbert",
        "Diane",
    ]

    last_names = [
        "Cole",
        "Harrison",
        "Weaver",
        "Moss",
        "Hawkins",
        "George",
        "Sanchez",
        "Holloway",
        "Guerrero",
        "Joseph",
    ]

    def get_zip():
        return int("".join((str(random.randint(0, 10)) for i in range(5))))

    def get_phone():
        area = "".join((str(random.randint(0, 10)) for i in range(3)))
        prefix = "".join((str(random.randint(0, 10)) for i in range(3)))
        local = "".join((str(random.randint(0, 10)) for i in range(4)))
        return "-".join((area, prefix, local))

    def get_registered(base_date=None):
        base_date = base_date or datetime.now()
        offset = random.randint(0, 1000)
        return base_date - timedelta(days=offset)

    base_date = datetime(2020, 1, 1)

    for first in first_names:
        for last in last_names:
            params = dict(
                name=f"{first} {last}",
                postal_code=get_zip(),
                phone=get_phone(),
                registered_at=date_to_str(get_registered(base_date)),
            )

            c = Customer(**params)
            db.session.add(c)

    db.session.commit()