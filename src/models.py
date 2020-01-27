from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    # date = db.Column(db.Integer, unique=False, nullable=False)
    petname = db.Column(db.String(120),unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.firstName

    def serialize(self):
        return {
            "firstName": self.firstName,
            "email": self.email,
            "password": self.password,
            "petname": self.petname
            # "date": self.date
    }
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return '<Login %r>' % User.firstName

    def serialize(self):
        return {
            "firstName": User.firstName,
            "email": User.email,
            "password": User.password,
            "petname": User.petname,
            # "date": User.date
    }
class Dogfile(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String(80), unique=False, nullable=False)
    dob = db.Column(db.String(60), unique=False, nullable=False)
    imglink = db.Column(db.String(120), unique=False, nullable=False)
    # user_id = db.Column(db.String(80), db.ForeignKey('user.id'),
        # nullable=False)
     
    def __repr__(self):
        return '<Dogfile %r>' % self.petname

    def serialize(self):
        return {
            "petname": self.petname,
            "dob": self.dob,
            "imglink": self.imglink
            # "user_id": self.user_id
    }

class GeneralRecords(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    vet_name = db.Column(db.String(80), unique=False, nullable=False)
    groomer_name = db.Column(db.String(80), unique=False, nullable=False)
    vet_address = db.Column(db.String(120), unique=False, nullable=False)
    groomer_address = db.Column(db.String(120), unique=False, nullable=False)
    insurance_policy = db.Column(db.String(120), unique=True, nullable=False)
    insurance_provider = db.Column(db.Integer, unique=False, nullable=False)
    petname = db.Column(db.String(80), unique=False, nullable=False)


    def __repr__(self):
        return '<GeneralRecords %r>' % self.petname

    def serialize(self):
        return {
            "vet_name": self.vet_name,
            "groomer_name": self.groomer_name,
            "vet_address": self.vet_address,
            "groomer_address": self.groomer_address,
            "insurance_policy": self.insurance_policy,
            "insurance_provider": self.insurance_provider,
            "petname": self.petname,
    }
