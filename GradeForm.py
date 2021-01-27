from wtforms import Form, SelectField, validators

class GradeForm(Form):
    grade = SelectField('Grade', [validators.DataRequired()], choices=[("",""),("S","S"),("A","A"),("B","B"),("C","C")], default="")
    priority = SelectField('Priority', [validators.DataRequired()],
                        choices=[("", ""), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")], default="")
