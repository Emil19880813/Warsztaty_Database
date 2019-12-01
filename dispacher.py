from typing import Union, List

from models import User, Message
from models import create_connection, get_cursor

class WrongParameterError(Exception):
    """Error when wrong params set is given"""
    pass


class Dispacher:

    """HINT: USERNAME == EMAIL """
    @staticmethod
    def create_user(username: str, password: str) -> User:
        connection = create_connection()
        cursor = get_cursor(connection)
        if User.get_by_username(cursor, username) == None:
            username = username
            hash_password = User.set_password(password)
            email = username
            user = User._create_user_object(username, hash_password, email)
            user.save(cursor)
        cursor.close()
        connection.close()
        raise NotImplementedError

    @staticmethod
    def login_user(username: str, hash_password: str) -> Union[User, None]:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        cursor.close()
        connection.close()
        if user and user.check_password(hash_password):
            return True
        """Check if user exist in database and return True if password is correct."""
        raise NotImplementedError

    @staticmethod
    def print_all_users() -> List[Union[User, None]]:
        """Print all users which are in database"""
        connection = create_connection()
        cursor = get_cursor(connection)
        all_users = User.get_all(cursor)
        cursor.close()
        connection.close()
        if all_users:
            raise NotImplementedError
        return all_users

    @staticmethod
    def change_password(username: User, password: str, new_password: str) -> None:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        if user and user.check_password(password):
            user.set_password(new_password)
            user.save(cursor)
            cursor.close()
            connection.close()
        """Chenge password of given user to new one"""
        raise NotImplementedError

    @staticmethod
    def delete_user(username: User, password) -> None:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        if user and user.check_password(password):
            user.delete(cursor)
            cursor.close()
            connection.close()
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
