
import argparse

from dispacher import Dispacher
from logic_handler import OptionsHandler
from models import create_connection, get_cursor, generate_salt

parser = argparse.ArgumentParser(description='Program options')
parser.add_argument('--username', '-u', help='Login - user email', action='store')
parser.add_argument('--password', '-p', help='User password', action='store')
parser.add_argument('--new-password', '-n', help='New password', action='store')
parser.add_argument('--edit', '-e', help='Edit', action='store_true')
parser.add_argument('--delete', '-d', help='Delete user', action='store_true')
parser.add_argument('--list', '-l', help='List of user or massages', action='store_true')
parser.add_argument('--send', '-s', help='Send', action='store')
parser.add_argument('--to', '-t', help='Address of message', action='store')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    dispacher = Dispacher()

    salt = generate_salt()
    connection = create_connection()
    cursor = get_cursor(connection)

    option_handler = OptionsHandler(
        args.password, args.username, args.new_password, args.edit, args.delete, args.list, args.send, args.to
    )

    if option_handler.create_user:
        dispacher.create_user(args.username, args.password, salt, cursor)
    elif option_handler.list_all_users:
        dispacher.print_all_users(cursor)
    elif option_handler.list_all_messages_for_user:
        dispacher.list_messages(cursor, args.username, args.password)
    elif option_handler.change_password:
        dispacher.change_password(args.username, args.password, args.new_password, salt, cursor)
    elif option_handler.send_message:
        dispacher.send_message(cursor, args.username, args.password, args.send, args.to)
    elif option_handler.delete_user:
        dispacher.delete_user(cursor, args.username, args.password)
    else:
        dispacher.not_available_option()

    cursor.close()
    connection.close()
