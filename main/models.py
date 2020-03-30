from datetime import datetime
from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    association_table = db.relationship('Address_association_table', backref='who')

    def __repr__(self):
        return f"Address('{self.address}', '{self.city}', '{self.state}')"


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=True)
    association_table = db.relationship('Address_association_table', backref='located')
    person_id = db.Column(db.Integer, db.ForeignKey('individual.id'), nullable=False)


class Address_association_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('individual.id'), nullable=True)
    work_id = db.Column(db.Integer, db.ForeignKey('work.id'), nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

    def __repr__(self):
        return f'<Association {self.person_id} {self.work_id} {self.address_id}>'


class Symptoms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cough = db.Column(db.Boolean, unique=False, default=False)
    fever = db.Column(db.Boolean, unique=False, default=False)
    how_hot = db.Column(db.Integer, unique=False, default=0)
    fatigue = db.Column(db.Boolean, unique=False, default=False)
    difficulty_breathing = db.Column(db.Boolean, unique=False, default=False)
    how_difficult = db.Column(db.Integer, unique=False, default=0)
    runny_nose = db.Column(db.Boolean, unique=False, default=False)
    body_aches = db.Column(db.Boolean, unique=False, default=False)
    headache = db.Column(db.Boolean, unique=False, default=False)
    stomach = db.Column(db.Boolean, unique=False, default=False)
    sore_throat = db.Column(db.Boolean, unique=False, default=False)
    how_long = db.Column(db.Integer, unique=False, default=0)
    person_id = db.Column(db.Integer, db.ForeignKey('individual.id'), nullable=False)


    def __repr__(self):
        all_true = []
        data = {'cough': self.cough, 'fever': self.fever, 'how_hot': self.how_hot,
                'fatigue': self.fatigue, 'difficulty_breathing': self.difficulty_breathing,
                'how_difficult': self.how_difficult, 'runny_nose': self.runny_nose,
                'body_aches': self.body_aches, 'headache': self.headache,
                'stomach': self.stomach, 'sore_throat': self.sore_throat,
                'how_long': self.how_long}

        for key, value in data.items():
            if value is True:
                all_true.append(key)
        return ', '.join(all_true)



class Individual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    association_table = db.relationship('Address_association_table', backref='home', lazy=True)
    work = db.relationship('Work', backref='employer_info', lazy=True)
    symptoms = db.relationship('Symptoms', backref='carries', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.name
