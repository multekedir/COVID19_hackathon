from main.person import Person
from main import db
from main.models import Individual, Address, Address_association_table, Work, Symptoms
from sqlalchemy import or_

db.drop_all()
db.create_all()


def add_person(new_person: Person) -> int:
    print('adding')
    # get the address for the person
    address_info = new_person.get_address
    work_contact = new_person.list_of_work[0]

    # create db instance
    print('create db instance')
    person = Individual(name=new_person.name, age=new_person.age, phone=new_person.phone, email=new_person.email)
    address = Address(address=address_info.address, city=address_info.city, state=address_info.state,
                      zip_code=address_info.zip_code)

    work_address = Address(address=work_contact['address'].address, city=work_contact['address'].city,
                           state=work_contact['address'].state,
                           zip_code=work_contact['address'].zip_code)

    # add new instance to db
    db.session.add(person)

    db.session.add_all([address, work_address])
    db.session.flush()
    person_id = person.id
    if check_work(work_contact['name'], work_contact['email'], work_contact['phone']):
        work = Work(employer=work_contact['name'], phone=work_contact['phone'], email=work_contact['email'],
                    person_id=person.id)
        db.session.add(work)
        db.session.flush()
        db.session.add(Address_association_table(person_id=None, work_id=work.id, address_id=work_address.id))

    db.session.add(Address_association_table(person_id=person.id, work_id=None, address_id=address.id))
    db.session.commit()
    return person_id


def check_work(name, email, phone):
    return db.session.query(Work.id).filter(or_(Work.email.like(email), Work.employer.like(name), Work.phone.like(phone))) is None



def add_symptoms(person: Person, person_id: int):
    symptoms = person.symptoms
    db.session.add(Symptoms(cough=symptoms['cough'], fever=symptoms['fever'], how_hot=(symptoms['how_hot']),
                            fatigue=symptoms['fatigue'], difficulty_breathing=symptoms['difficulty_breathing'],
                            how_difficult=symptoms['how_difficult'], runny_nose=symptoms['runny_nose'],
                            body_aches=symptoms['body_aches'], headache=symptoms['headache'],
                            stomach=symptoms['stomach'], sore_throat=symptoms['sore_throat'],
                            how_long=symptoms['how_long'], person_id=person_id))
    db.session.commit()
    db.session.close()

# def get_items(name, age_min, age_max, symptoms, temp_min, temp_max, pain_min, pain_max, num_of_days_min, num_ofdays_max):
def get_items():
    print()
    return Individual.query.all()
def get_person(p_id) -> Individual:

    return db.session.query(Individual).filter(Individual.id == p_id).first()


def rollback():
    db.session.rollback()
    db.session.close()
