from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, SubmitField, IntegerField, PasswordField, TimeField
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired
import phonenumbers

class CreateReservationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=8,max=200), validators.DataRequired()])
    contact = TelField('Contact no.', [validators.length(min=1, max=30), validators.DataRequired()])
    date = DateField('DATE', format='%d-%m-%Y')
    time_slot = TimeField('Time')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateReviewForm(Form):
    reviewfeedback = TextAreaField('Testimonals from customers', [validators.Optional()])
    reviewfirst_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    reviewlast_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])


class GuestBooking(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    industry = SelectField('Industry', [validators.DataRequired()],
                           choices=[], default="")
    occupation = SelectField('Occupation', [validators.DataRequired()],
                             choices=[], default="")
    location = SelectField("Location of Workplace", [validators.DataRequired()], choices=[], default="")
    transport = RadioField('Transport Required?', choices=[('Yes', 'Yes'), ('No', 'No')], default='Y')


class BookingForm(FlaskForm):
    bookindate = DateField('CHECK-IN DATE', format='%Y-%m-%d')
    bookoutdate = DateField('CHECK-OUT DATE', format='%Y-%m-%d')
    submit = SubmitField('Submit')


class GradeForm(Form):
    grade = SelectField('Grade', [validators.DataRequired()],
                        choices=[("", ""), ("S", "S"), ("A", "A"), ("B", "B"), ("C", "C")], default="")
    priority = SelectField('Priority', [validators.DataRequired()],
                           choices=[("", ""), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")], default="")


class HospitalForm(Form):
    hospital_beds = IntegerField('Number of Beds', [validators.required()])
    hospital_contact = StringField('Contact Number', [validators.Length(9), validators.DataRequired()])


class OccupationForm(Form):
    occupation_name = StringField('Occupation', [validators.Length(min=1, max=150), validators.DataRequired()])
    occupation_industry = SelectField('Industry', [validators.DataRequired()],
                                      choices=[], default="")
    description = TextAreaField('Description', [validators.Optional()])

class VehicleForm(Form):
    vehicle_name = StringField("Driver's Name", [validators.Length(min=1, max=150), validators.DataRequired()])
    vehicle_model = StringField('Vehicle Model:', )
    vehicle_car_plate = StringField('License Plate no.', )
    vehicle_contact = StringField('Contact Number', [validators.Length(9), validators.DataRequired()])
    vehicle_location = SelectField('Assign Hospital Location', [validators.DataRequired()],
                           choices=[], default="")


class IndustryForm(Form):
    industry_name = StringField('Industry', [validators.Length(min=1, max=150), validators.DataRequired()])


class RequestForm(Form):
    type = SelectField('Request Type', [validators.DataRequired()],
                       choices=[("", ""), ("Normal", "Normal"), ("Urgent", "Urgent")], default="")
    topic = StringField('Request Topic', [validators.Length(min=1, max=150), validators.DataRequired()])
    details = TextAreaField('Details', [validators.Optional()])


class ChooseGuest(Form):
    guest_name = SelectField("Guest Name", [validators.DataRequired()], choices=[], default="")


class CreateProductForm(Form):
    productcat = StringField("New Product Category", [validators.Length(min=1, max=150), validators.DataRequired()])


class CreateSupplierForm(Form):
    company_name = StringField('Company Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    uen_number = IntegerField('UEN Number', [validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    product_name = SelectField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])


class CreateInventoryForm(Form):
    item_name = StringField('Item Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    supplier = SelectField('Supplier', [validators.DataRequired()], choices=[], default='')
    product_name = SelectField('Product Name', [validators.DataRequired()], choices=[], default='')
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1), validators.DataRequired()])


class CreateOrderForm(Form):
    item_name = SelectField('Item Name', [validators.DataRequired()], choices=[], default='')
    product_name = SelectField('Product Name', [validators.DataRequired()], choices=[], default='')
    supplier = SelectField('Supplier', [validators.DataRequired()], choices=[], default='')
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])


class CreatePartnershipsForm(Form):
    company = StringField('Company', [validators.Length(min=1, max=150), validators.DataRequired()])
    resources = StringField('Resources', [validators.Length(min=1, max=150), validators.DataRequired()])
    industry = StringField('Industry', [validators.Length(min=1, max=150), validators.DataRequired()])


class CreatePackageDeal(Form):
    attractions = StringField('Attraction', [validators.Length(min=1, max=150), validators.DataRequired()])
    transport = StringField('Transport', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = StringField('Price', [validators.Length(min=1, max=150), validators.DataRequired()])
    code = StringField('Code', [validators.Length(min=1, max=150), validators.DataRequired()])


class Login(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = StringField('Password', [ validators.DataRequired()])


class Signup(Form):
    name = StringField('Name', [ validators.DataRequired()])
    username = StringField('Username', [ validators.DataRequired()])
    email = StringField('Email', [ validators.DataRequired()])
    phone_num = IntegerField('Phone Number', [ validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')] , default='')
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('repeat_password', message ='Incorrect Password')])
    repeat_password = PasswordField('Repeat Password')
    deals = SelectField('Package Deals', choices=[('ZWM', 'Zoo Wee Mama'), ('MCF', 'Middle Class Fun'), ('KL', 'Kinda Loaded'), ('SA', 'Spend Away'), ('WIT', 'What In The-')])

class Staff_Login(Form):
    id = IntegerField('ID', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])

class Staff_Signup(Form):
    id = IntegerField('ID', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('repeat_password', message='Incorrect password')])
    repeat_password = PasswordField('Repeat Password')


# class RoomForm(Form):
#
