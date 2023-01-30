import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: str
    birthday_day: str
    birthday_month: str
    birthday_year: str
    subject: str
    hobby: str
    photo: str
    adress: str
    state: str
    city: str

