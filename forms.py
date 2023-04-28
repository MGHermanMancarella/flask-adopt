"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired()]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[InputRequired(), URL()]
    )

    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=["baby", "young", "adult", "senior"]
    )

    notes = StringField("Notes")