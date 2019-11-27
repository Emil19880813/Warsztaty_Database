class OptionsHandler:
    def __init__(self, password, username, new_password, edit, delete, list, send, to):
        self.password = bool(password)
        self.username = bool(username)
        self.new_password = bool(new_password)
        self.edit = bool(edit)
        self.delete = bool(delete)
        self.list = bool(list)
        self.send = bool(send)
        self.to = bool(to)

    @property
    def _login_provided(self) -> bool:
        return self.username and self.password

    @property
    def create_user(self) -> bool:
        return self._login_provided and \
               not any([self.new_password, self.edit, self.delete, self.list, self.send, self.to])

    @property
    def list_all_users(self) -> bool:
        return self.list and \
               not any([self.new_password, self.edit, self.delete, self.username, self.password, self.send, self.to])

    @property
    def list_all_messages_for_user(self) -> bool:
        return self.list and \
               self._login_provided and \
               not any([self.new_password, self.edit, self.delete, self.send, self.to])

    @property
    def change_password(self) -> bool:
        return self._login_provided and \
               self.edit and \
               self.new_password and \
               not any([self.delete, self.send, self.to, self.list])

    @property
    def send_message(self) -> bool:
        return self._login_provided and \
               self.send and \
               self.to and \
               not any([self.list, self.delete, self.edit, self.new_password])

    @property
    def delete_user(self) -> bool:
        return self._login_provided and \
               self.delete and \
               not any([self.send, self.to, self.list, self.new_password, self.edit])
