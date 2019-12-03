from typing import Union, List

from models import User, Message
from models import create_connection, get_cursor
from datetime import datetime

class WrongParameterError(Exception):
    """Error when wrong params set is given"""
    pass


class Dispacher:

    """HINT: USERNAME == EMAIL """
    @staticmethod
    def create_user(username: str, password: str) -> User:
        connection = create_connection()
        cursor = get_cursor(connection)
        if not User.get_by_username(cursor, username):
            user = User._create_user_object(username, password, username)
            user.save(cursor)
            cursor.close()
            connection.close()
        else:
            raise WrongParameterError("This user already exist!")

    @staticmethod
    def login_user(username: str, hash_password: str) -> Union[User, None]:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        cursor.close()
        connection.close()
        if user and user.check_password(hash_password):
            return True
        else:
            raise WrongParameterError("Wrong login or password!")


    @staticmethod
    def print_all_users() -> List[Union[User, None]]:
        """Print all users which are in database"""
        connection = create_connection()
        cursor = get_cursor(connection)
        all_users = User.get_all(cursor)
        cursor.close()
        connection.close()
        if all_users:
            return all_users
        else:
            raise WrongParameterError("There is no users!")

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
        else:
            raise WrongParameterError("Wrong login or password!")

    @staticmethod
    def delete_user(username: User, password) -> None:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        if user and user.check_password(password):
            user.delete(cursor)
            cursor.close()
            connection.close()
        else:
            raise WrongParameterError("Wrong login or password!")

    @staticmethod
    def list_messages_to_user(username, password, to_id) -> List[Union[Message, None]]:
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        if user and user.check_password(password):
            messages = Message.load_all_messages_for_user(cursor, to_id, user.id)
            cursor.close()
            connection.close()
            return messages
        else:
            raise WrongParameterError("Wrong login or password!")

    @staticmethod
    def send_message(username, password, to_id, text) -> Message:
        """Create message to adress (User) to sender (User) into database."""
        connection = create_connection()
        cursor = get_cursor(connection)
        user = User.get_by_username(cursor, username)
        if user and user.check_password(password):
            message = Message()
            message._id = -1
            message.from_id = user.id
            message.to_id = to_id
            message.tekst = text
            message.creation_date = datetime.now()
            message.save()
        else:
            raise WrongParameterError("Wrong login or password!")

    def not_available_option(self):
        """No other available option"""
        raise WrongParameterError("Wrong parameters set up!")
