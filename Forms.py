from wtforms import *
from flask_wtf import FlaskForm
from wtforms.fields.html5 import *
from wtforms.validators import DataRequired
import phonenumbers
import shelve

class CreateReservationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=8,max=200), validators.DataRequired()])
    contact = TelField('Contact no.', [validators.length(min=1, max=30), validators.DataRequired()])
    time_slot = TimeField('Time')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class ReservationDateForm(FlaskForm):
    date = DateField('DATE', format='%Y-%m-%d')

class CreateReviewForm(Form):
    reviewfeedback = TextAreaField('Testimonals from customers', [validators.Optional()])
    reviewfirst_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    reviewlast_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])


class GuestBooking(Form):
    industry = SelectField('Industry', [validators.DataRequired()],
                           choices=[], default="")
    occupation = SelectField('Occupation', [validators.DataRequired()],
                             choices=[], default="")
    location = SelectField("Location of Workplace", [validators.DataRequired()], choices=[], default="")
    transport = RadioField('Transport Required?', choices=[('Yes', 'Yes'), ('No', 'No')], default='Y')


class BookingForm(FlaskForm):
    bookindate = DateField('Check-In Date', format='%Y-%m-%d')
    bookoutdate = DateField('Check-Out Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

    def validate_bookindate(form, field):
        if field.data=="":
            raise ValidationError("Enter a book in date.")

    def validate_bookoutdate(form, field):
        if field.data == "":
            raise ValidationError("Enter a book out date.")


class BookRoomType(Form):
    room_type = SelectField('Room Type',
                        choices=[("", ""), ("Small Room", "Small Room"), ("Apartment", "Apartment"), ("Big Apartment", "Big Apartment"), ("Villa", "Villa")], default="")
    room_number= IntegerField('Room Number', [validators.required()])


class GradeForm(Form):
    grade = SelectField('Grade',
                        choices=[("", ""), ("S", "S"), ("A", "A"), ("B", "B"), ("C", "C")], default="")
    priority = SelectField('Priority',
                           choices=[("", ""), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")], default="")

    def validate_grade(form,field):
        if field.data=="":
            raise ValidationError("Grade cannot be empty.")

    def validate_priority(form, field):
        if field.data == "":
            raise ValidationError("Priority cannot be empty.")



class HospitalForm(Form):
    hospital_name = StringField('Hospital Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    hospital_address = StringField('Address', [validators.Length(min=1, max=150), validators.DataRequired()])
    hospital_beds = IntegerField('Number of Beds', [validators.required()])
    hospital_contact = StringField('Contact Number', [validators.DataRequired()])

    def validate_hospital_name(form,field):
        hospital_list=[]
        hospitaldb = shelve.open("hospital.db")
        hospital_list = hospitaldb["Hospital_choices"]
        for hospitals in hospital_list:
            if field.data == hospitals:
                raise ValidationError("Existing hospital in database. Search for another hospital.")

    # def validate_hospital_contact(form,field):
    #     if len(field.data) > 9:
    #         raise ValidationError("Invalid Contact Number. Try again.")
    #     try:
    #         x=phonenumbers.parse(field.data)
    #




class OccupationForm(Form):
    occupation_name = StringField('Occupation', [validators.Length(min=1, max=30), validators.DataRequired()])
    occupation_industry = SelectField('Industry', [validators.DataRequired()],
                                      choices=[], default="")
    description = TextAreaField('Description', [validators.Optional()])

    def validate_occupation_name(form, field):
        occupation_list = []
        occupationdb = shelve.open("occupation.db")
        occupation_list = occupationdb["Occupation_choices"]
        for occupations in occupation_list:
            if field.data == occupations:
                raise ValidationError("Existing occupation in database. Enter a different occupation.")


class OccupationEditForm(Form):
    occupation_name = StringField('Occupation', [validators.Length(min=1, max=30), validators.DataRequired()])
    occupation_industry = SelectField('Industry', [validators.DataRequired()],
                                      choices=[], default="")
    description = TextAreaField('Description', [validators.Optional()])




class VehicleForm(Form):
    vehicle_name = StringField("Driver's Name", [validators.Length(min=1, max=150), validators.DataRequired()])
    vehicle_model = StringField('Vehicle Model:', )
    vehicle_car_plate = StringField('License Plate no.', )
    vehicle_contact = StringField('Contact Number', [validators.Length(8), validators.DataRequired()])
    vehicle_location = SelectField('Assign Hospital Location', [validators.DataRequired()],
                           choices=[], default="")


class IndustryForm(Form):
    industry_name = StringField('Industry', [validators.Length(min=1, max=150), validators.DataRequired()])

    def validate_industry_name(form, field):
        industry_list = []
        occupationdb = shelve.open("occupation.db")
        industry_list = occupationdb["Industry_choices"]
        for industries in industry_list:
            if field.data == industries:
                raise ValidationError("Existing industry in database. Enter a different industry.")


class RequestForm(Form):
    type = SelectField('Request Type', [validators.DataRequired()],
                       choices=[("", ""), ("Normal", "Normal"), ("Urgent", "Urgent")], default="")
    topic = StringField('Request Topic', [validators.Length(min=1, max=150), validators.DataRequired()])
    details = TextAreaField('Details', [validators.Optional()])


class ChooseGuest(Form):
    guest_name = SelectField("Guest Name", [validators.DataRequired()], choices=[], default="")


class CreateProductForm(Form):
    product_name = StringField("New Product Name", [validators.Length(min=1, max=150), validators.DataRequired()])


class CreateSupplierForm(Form):
    company_name = StringField('Company Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    uen_number = IntegerField('UEN Number', [validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    product_name = SelectMultipleField('Product Name', [validators.DataRequired()])


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
    password = PasswordField('Password', [ validators.DataRequired()])


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
    password = PasswordField('Password', [validators.DataRequired()])

class Staff_Signup(Form):
    id = IntegerField('ID', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('repeat_password', message='Incorrect password')])
    repeat_password = PasswordField('Repeat Password')


# class RoomForm(Form):
#
