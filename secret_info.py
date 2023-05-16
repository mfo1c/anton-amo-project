from dataclasses import dataclass
import os


@dataclass()
class SecretInfo:
    login: str
    password: str
    account_url: str


env_info = SecretInfo(
        login=os.getenv('login'),
        password=os.getenv('password'),
        account_url=os.getenv('account_url')
    )