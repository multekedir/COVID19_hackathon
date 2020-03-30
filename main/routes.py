from flask import render_template, flash, redirect, url_for
from main import app
from main.forms import PersonalInfo, FilterForm
from main.person import Address, Person
from main.controller import add_person, rollback, add_symptoms, get_items, get_person
from sqlalchemy.exc import IntegrityError


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return 'about'


@app.route("/request", methods=['GET', 'POST'])
def request():
    form_personal = PersonalInfo()

    if form_personal.validate_on_submit():
        personal_address = Address(form_personal.contact.address.data, form_personal.contact.apt.data,
                                   form_personal.contact.state.data,
                                   form_personal.contact.city.data, form_personal.contact.zip_code.data)

        work_address = Address(form_personal.employer_contact.address.data, form_personal.employer_contact.apt.data,
                               form_personal.employer_contact.state.data,
                               form_personal.employer_contact.city.data, form_personal.employer_contact.zip_code.data)

        who = Person(form_personal.first_name.data, form_personal.last_name.data, form_personal.age.data,
                     form_personal.contact.phone.data, form_personal.contact.email.data, personal_address)

        who.add_work(form_personal.employer.data, form_personal.employer_contact.phone.data,
                     form_personal.employer_contact.email.data, work_address)

        who.add_symptoms(form_personal.symptoms.data)
        print(form_personal.symptoms.data)

        try:

            new_person_id = add_person(who)
            print("added new person")
            add_symptoms(who, new_person_id)
        except IntegrityError:
            flash(f'A person with that email or phone is in the system', 'danger')
            rollback()
        else:
            flash(f'Request submitted', 'success')
            return redirect(url_for('home'))

    return render_template('personal_info.html', title='Request Testing', form=form_personal)


@app.route("/view")
def view():
    filter_form = FilterForm()
    return render_template('view_data.html', form=filter_form)


@app.route("/view", methods=['POST'])
def post_view():
    filter_form = FilterForm()

    return render_template('view_data.html', form=filter_form, items=get_items())


@app.route("/person/<p_id>", methods=['GET'])
def show_person(p_id):

    return render_template('person.html', person=get_person(int(p_id)))
