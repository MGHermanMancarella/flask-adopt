"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from forms import PET_AGES, SPECIES_LIST

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    '''pets.'''

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(20),
        nullable=False
    )

    species = db.Column(
        db.String(20),
        db.CheckConstraint(f"species in {SPECIES_LIST}"),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    age = db.Column(
        db.String(6),
        db.CheckConstraint(f"age in {PET_AGES}"),
        nullable=False
    )

    notes = db.Column(
        db.Text,
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )