from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators

from .models import Transaction


class TransactionForm(FlaskForm):
    value = IntegerField(label='Transaction value', validators=[validators.DataRequired()])
    status = StringField(label='Transaction satus')
    unit = StringField(label='Transaction Unit (Ex: $, Euro,Soms)', validators=[validators.DataRequired()])
    comment = StringField(label='Comments', validators=[validators.DataRequired()])
    submit = SubmitField(label='Save transaction')

