from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class GuestBooking(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    industry = SelectField('Industry', [validators.DataRequired()], choices=[("",""),("Medical","Medical"),("Others","Others")], default="")
    occupation = SelectField('Occupation', [validators.DataRequired()], choices=[("none",""),("Doctor", "Doctor"),( "Paramedic" ,"Paramedic"),( "Registered Nurse","Registered Nurse"),( "Patient Care Assistant","Patient Care Assistant"),( "Family and General Practitioner","Family and General Practitioner"),("Others", "Others")], default="")
    location = SelectField("Location of Workplace",[validators.DataRequired()], choices=[], default="")
    transport = RadioField('Transport Required?', choices=[('Yes', 'Yes'), ('No', 'No')],default='Y')