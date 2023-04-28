"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

PET_AGES = ("baby", "young", "adult", "senior")
SPECIES_LIST = ("cat", "dog", "porcupine")

class AddPetForm(FlaskForm):
    '''Form to save a life'''

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        validators=[InputRequired()],
        choices=SPECIES_LIST
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=PET_AGES
    )

    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    '''Edit pet information'''

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = StringField("Notes")

    available = BooleanField("Available")