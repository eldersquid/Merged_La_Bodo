from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, SubmitField, IntegerField, \
    BooleanField, ValidationError, TimeField
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
    date = StringField('Date')
    time_slot = TimeField('Time')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateReviewForm(Form):
    reviewfeedback = TextAreaField('Testimonals from customers', [validators.Optional()])
    reviewfirst_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    reviewlast_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])


class GuestBooking(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    industry = SelectField('Industry', [validators.DataRequired()],
                           choices=[("", ""), ("Medical", "Medical"), ("Others", "Others")], default="")
    occupation = SelectField('Occupation', [validators.DataRequired()],
                             choices=[("none", ""), ("Doctor", "Doctor"), ("Paramedic", "Paramedic"),
                                      ("Registered Nurse", "Registered Nurse"),
                                      ("Patient Care Assistant", "Patient Care Assistant"),
                                      ("Family and General Practitioner", "Family and General Practitioner"),
                                      ("Others", "Others")], default="")
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
    hospital_name = StringField('Hospital Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    hospital_address = StringField('Address', [validators.Length(min=1, max=150), validators.DataRequired()])
    hospital_beds = IntegerField('Number of Beds', [validators.required()])
    hospital_contact = StringField('Contact Number', [validators.Length(9), validators.DataRequired()])


class OccupationForm(Form):
    occupation_name = StringField('Occupation', [validators.Length(min=1, max=150), validators.DataRequired()])
    occupation_industry = StringField('Industry', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Optional()])

class VehicleForm(Form):
    vehicle_name = StringField("Driver's Name", [validators.Length(min=1, max=150), validators.DataRequired()])
    vehicle_model = StringField('Vehicle Model:', )
    vehicle_car_plate = StringField('License Plate no.', )
    vehicle_contact = StringField('Contact Number', [validators.Length(9), validators.DataRequired()])
    vehicle_location = SelectField('Assign Hospital Location', [validators.DataRequired()],
                           choices=[], default="")


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
    product_name = SelectField('Product Name', [validators.DataRequired()], choices=[], default='Select')


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
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])


class Signup(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    password = StringField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    repeat_password = StringField('Repeat Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 28. 2420)',
                              [validators.DataRequired()])

# class RoomForm(Form):
#
