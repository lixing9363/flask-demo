from apps import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"<User id={self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            # "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }

