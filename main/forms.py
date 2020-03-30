from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FormField, Form, BooleanField
from wtforms.validators import DataRequired, Email, NumberRange, Length


class ContactInfo(Form):
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10)])
    email = StringField('Email', validators=[Email(message='Not a valid email')])
    address = StringField('Address', validators=[DataRequired()])
    apt = StringField('Address 2')
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = IntegerField('Zip', validators=[DataRequired()])


class Symptoms(Form):
    cough = BooleanField('Cough')
    fever = BooleanField('Fever')
    how_hot = IntegerField('What is your oral temperature in °F right now', validators=[NumberRange(min=80, max=200)])
    fatigue = BooleanField('Fatigue')
    difficulty_breathing = BooleanField('Difficulty Breathing')
    how_difficult = IntegerField('How hard is it to breath 1 = low; 10 = very difficult',
                                 validators=[NumberRange(min=0, max=10)])
    runny_nose = BooleanField('Runny Nose')
    body_aches = BooleanField('Body Aches')
    headache = BooleanField('Headache')
    stomach = BooleanField('Stomach Issue')
    sore_throat = BooleanField('Sore Throat')
    how_long = IntegerField('How many days have you had these symptoms')


class PersonalInfo(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, message='You have to be an adult')])
    contact = FormField(ContactInfo)
    employer = StringField('Employer', validators=[DataRequired()])
    employer_contact = FormField(ContactInfo)
    symptoms = FormField(Symptoms)
    submit = SubmitField('Next')


class FilterForm(FlaskForm):
    name = StringField('Name')
    body_temp_upper = IntegerField('_',validators=[NumberRange(min=80, max=200)])
    body_temp_lower = IntegerField('Body Heat', validators=[NumberRange(min=90, max=110)])
    difficulty_upper = IntegerField('_', validators=[NumberRange(min=0, max=10)])
    difficulty_lower = IntegerField('Pain Level', validators=[NumberRange(min=0, max=10)])
    age_upper = IntegerField('_', validators=[NumberRange(min=18)])
    age_lower = IntegerField('Age', validators=[NumberRange(min=18)])
    how_long_upper = IntegerField('_', validators=[NumberRange(min=90, max=110)])
    how_long_lower = IntegerField('Number of days',
                                  validators=[NumberRange(min=90, max=110)])
    symptoms = FormField(Symptoms)
    search = SubmitField('Search ')
