from flask import Flask, render_template, request, flash, redirect, url_for
#from flask_restful import Resource, fields, marshal_with, Api
import click
import requests
from functions import get_books

from models import create_tables, drop_tables, User, Publication
#from forms import DinosaurForm


app = Flask(__name__)
"""app.secret_key = 'Hello WOrld' # Don't use it !
api = Api(app)

@app.route('/books')
def books():
    books = get_books()
    return render_template('books.html', books=books)


dinosaur_fields = {
    'name': fields.String,
    'birthday': fields.String,
}

class DinosaurAPI(Resource):
    @marshal_with(dinosaur_fields)
    def get(self):
        return [d for d in Dinosaur.select()]

api.add_resource(DinosaurAPI, '/api/dinosaurs/')

@app.route('/')
def dinosaurs():
    dinosaurs = Dinosaur.select()
    return render_template('dinosaurs/list.html', dinosaurs=dinosaurs)


@app.route('/dinosaurs/<int:id>')
def dinosaur_detail(id):
    dinosaur = Dinosaur.get(id)
    return render_template('dinosaurs/details.html', dinosaur=dinosaur)


@app.route('/dinosaurs/form/', methods=['GET', 'POST', ])
@app.route('/dinosaurs/form/<int:id>', methods=['GET', 'POST', ])
def dinosaur_form(id=None):
    if id:
        dinosaur = Dinosaur.get(id)
    else:
        dinosaur = Dinosaur()
    
    if request.method == 'POST':
        form = DinosaurForm(request.form, obj=dinosaur) if id else DinosaurForm(request.form)
        if form.validate():
            form.populate_obj(dinosaur)
            dinosaur.save()
            flash('Your dinosaur has been saved')
            return redirect(url_for('dinosaurs'))
    else:
        form = DinosaurForm(obj=dinosaur) if id else DinosaurForm()
    return render_template('dinosaurs/form.html', form=form, dinosaur=dinosaur)


@app.route('/species/')
def species():
    species = Specie.select()
    return render_template('species/list.html', species=species)

"""
@app.cli.command()
def initdb():
    create_tables()
    click.echo('Database created')


@app.cli.command()
def dropdb():
    drop_tables()
    click.echo('Database dropped')


@app.cli.command()
def fakedata():
    from faker import Faker
    fake = Faker()
    for user_ex in range(0, 3):
        user = User.create(username=fake.last_name(), first_name = fake.first_name(), last_name=fake.last_name(), email = fake.email())
        for publications_ex in range(0, 3):
            publication = Publication.create(title = "Titre", body = fake.text(),
                                      user_created=user)

@app.cli.command()
def testdb():
    for dino in User.select():
        for publi in Publication.select():
            if publi.user_created == dino:
                print(dino.username + " " + publi.body)

