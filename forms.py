"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        validators=[InputRequired()],
        choices=["cat", "dog", "porcupine"]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=["baby", "young", "adult", "senior"]
    )

    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = StringField("Notes")

    available = BooleanField("Available")