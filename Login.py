from sqlalchemy.testing.pickleable import User


class Staff:
    def __init__(self, staff_id, username, password):
        self.staff_id = staff_id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id = 1, username = 'Gabriel', password = 'password'))

print(users)