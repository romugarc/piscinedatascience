import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id function"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


def form_login(name: str, surname: str) -> str:
    """form_login function"""
    return name[0:1] + surname


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = form_login(self.name, self.surname)
        self.id = generate_id()
