 from typing import Union, List

from models import User, Message


class WrongParameterError(Exception):
    """Error when wrong params set is given"""
    pass


class Dispacher:
    """HINT: USERNAME == EMAIL """
    def create_user(self, username: str, password: str) -> User:
        """Create user to User table"""
        raise NotImplementedError

    def login_user(self, username: str, password: str) -> Union[User, None]:
        """Check if user exist in database and return True if password is correct."""
        raise NotImplementedError

    def print_all_users(self) -> List[Union[User, None]]:
        """Print all users which are in database"""
        raise NotImplementedError

    def change_password(self, user: User, new_password: str) -> None:
        """Chenge password of given user to new one"""
        raise NotImplementedError

    def delete_user(self, user: User) -> None:
        """Delete given user"""
        raise NotImplementedError

    def list_messages_to_user(self, user: User) -> List[Union[Message, None]]:
        """Return list of all messages in database for specific user"""
        raise NotImplementedError

    def send_message(self, adress: User, sender: User, message: str) -> Message:
        """Create message to adress (User) to sender (User) into database."""
        raise NotImplementedError

    def not_available_option(self):
        """No other available option"""
        raise WrongParameterError("Wrong parameters set up!")
