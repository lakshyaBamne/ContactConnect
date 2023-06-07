from flaskr import db

class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.String(64), primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        """
            string representation of the User Table
        """
        return f'<User {self.username}>'
    
class UserData(db.Model):
    __tablename__ = "user_data"
    username = db.Column(db.String(64), db.ForeignKey('user.username'), primary_key=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128))
    contact = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """
            string representation of the UserData Table
        """
        return f'<UserData username[{self.username}] name[{self.name}] email[{self.email}] contact[{self.contact}]>'

class UserContacts(db.Model):
    __tablename__ = "user_contacts"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128))
    contact = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        """
            string representation of the UserContacts Table
        """
        return f'<UserContacts for all users>'