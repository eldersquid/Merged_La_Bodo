from wtforms import Form, StringField, TextAreaField, validators, TimeField
from wtforms.fields.html5 import EmailField, TelField



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
