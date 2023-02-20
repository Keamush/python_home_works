import hashlib

from faker import Faker
from faker.providers import BaseProvider
from password_generator import PasswordGenerator
from random import choice
from typing import NamedTuple


class ProfileDTO(NamedTuple):
    username: str
    email: str
    password: str
    info: str
    avatar: str
    role: str


fake = Faker()


class RoleProvider(BaseProvider):
    roles = ('user', 'admin')

    def role(self) -> str:
        return choice(self.roles)


fake.add_provider(RoleProvider)


def generate_password():
    generator = PasswordGenerator()
    generator.minlen = 10
    return generator.generate()


def generate_avatar(email: str) -> str:
    email_hash = hashlib.md5(email.encode()).hexdigest()
    url = f'https://www.gravatar.com/avatar/{email_hash}?d=identicon'
    return url


def generate_profiles(qty: int) -> list[ProfileDTO]:
    profiles = []
    for _ in range(qty):
        profile = fake.profile()
        role = fake.role()
        username = profile['username']
        email = profile['mail']
        info = profile['job']
        password = generate_password()
        avatar = generate_avatar(email)

        profiles.append(
            ProfileDTO(username, email, password, info, avatar, role)
        )
    return profiles

