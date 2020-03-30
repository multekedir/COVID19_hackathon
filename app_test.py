from main import app
from main import db
from main.controller import add_person, add_symptoms
from main.person import Person, Address


db.create_all()

home_1 = Address("2071 Harron Drive", '',  'MD', 'Columbia',  "21044")
work_add_1 = Address('1600 Amphitheatre Parkway', '','Mountain View', 'CA' ,'94043')

fake_1 = Person('Esther', 'Jones', 53,'4435469206','EstherWJones@jourrapide.com', home_1)
fake_1.add_work('google','9185584730', 'djshgfhsgfhd@gmail.com',work_add_1)
fake_1.add_symptoms({'cough': True, 'fever': False, 'how_hot': 90, 'fatigue': False, 'difficulty_breathing': True,
                     'how_difficult': 8, 'runny_nose': False, 'body_aches': True, 'headache': False, 'stomach': False,
                     'sore_throat': False, 'how_long': 6})
new_person_id = add_person(fake_1)
add_symptoms(fake_1, new_person_id)
print('created fake 1')

home_2 = Address("1059 Camel Back Road", '2', 'OK', 'Tulsa', "74119")


fake_2 = Person('Frank', 'Harrison', 20,'7885469206','FrankDHarrison@jourrapide.com', home_2)
fake_2.add_work('google','9185584730', 'djshgfhsgfhd@gmail.com', work_add_1)
fake_2.add_symptoms({'cough': True, 'fever': True, 'how_hot': 99, 'fatigue': True, 'difficulty_breathing': True,
                     'how_difficult': 3, 'runny_nose': True, 'body_aches': True, 'headache': False, 'stomach': False,
                     'sore_throat': False, 'how_long': 2})
new_person_id = add_person(fake_2)
add_symptoms(fake_2, new_person_id)
print('created fake 2')

fake_3 = Person('John', 'Kelly', 30,'6606872014','JohnMKelly@teleworm.us', home_2)
fake_3.add_work('Facebook','9185584730', 'djshgfhsgfhd@gmail.com', work_add_1)
fake_3.add_symptoms({'cough': False, 'fever': True, 'how_hot': 99, 'fatigue': True, 'difficulty_breathing': False,
                     'how_difficult': 1, 'runny_nose': True, 'body_aches': False, 'headache': True, 'stomach': True,
                     'sore_throat': False, 'how_long': 10})
new_person_id = add_person(fake_3)
add_symptoms(fake_3, new_person_id)

print('created fake 3')

home_4 = Address("3588 Broad Street", '66B', 'AL', 'Birmingham', "35203")


fake_4 = Person('Latoya', 'Freeman', 53,'19','LatoyaCFreeman@jourrapide.com', home_4)
fake_4.add_work('google','9185584730', 'djshgfhsgfhd@gmail.com', work_add_1)
fake_4.add_symptoms({'cough': True, 'fever': False, 'how_hot': 90, 'fatigue': True, 'difficulty_breathing': False,
                     'how_difficult': 7, 'runny_nose': False, 'body_aches': False, 'headache': True, 'stomach': True,
                     'sore_throat': True, 'how_long': 1})
new_person_id = add_person(fake_4)
add_symptoms(fake_4, new_person_id)
print('created fake 4')

home_5 = Address("3368 Willison Street", '',  'MN', 'Minneapolis', "55415")


fake_5 = Person('Betty', 'Primmer', 42,'7632382303','BettyJPrimmer@armyspy.com', home_1)
fake_5.add_work('AWS','9185584730', 'djshgfhsgfhd@gmail.com',  work_add_1)
fake_5.add_symptoms({'cough': True, 'fever': True, 'how_hot': 100, 'fatigue': True, 'difficulty_breathing': True,
                     'how_difficult': 7, 'runny_nose': False, 'body_aches': False, 'headache': False, 'stomach': False,
                     'sore_throat': True, 'how_long': 6})

new_person_id = add_person(fake_5)
add_symptoms(fake_5, new_person_id)
print('created fake 5')

if __name__ == '__main__':
    app.run(debug=False)
