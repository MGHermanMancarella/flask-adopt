"""Flask app for adopt app."""

import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def render_home():
    """displays the homepage"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        species = form.species.data
        photo = form.photo_url.data
        notes = form.notes.data
        new_pet = Pet(age=age, species=species, photo_url=photo, notes=notes, name=name)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"{name} added to adoption list!")
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)

