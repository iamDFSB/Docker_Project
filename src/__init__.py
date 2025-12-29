from sqlalchemy import select
from .config import DBConnection
from .entities import Users as UsersModel


class UserRepo:
    def insert_user(self, name):
        with DBConnection() as db:
            new_user = UsersModel(name=name)
            print(f"{new_user.name} - {new_user.id}")
            db.session.add(new_user)
            db.session.commit()

    def get_users(self):
        with DBConnection() as db:
            result = db.session.scalars(
                select(UsersModel)
            ).all()
            return result

