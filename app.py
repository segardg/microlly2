from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
import requests
import click
from functions import get_books
from playhouse.flask_utils import object_list

from models import create_tables, drop_tables, User, Publication
from forms import PublicationForm, UserForm, LoginForm


app = Flask(__name__)
app.secret_key = 'a6f8h2d971jk' 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users_login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
@app.route('/<username>') #username plutôt que id parce que c'est mieux de voir le username dans le lien
@login_required
def publication(username=None):
    publications = Publication.select()
    return object_list('publications/list.html', publications, paginate_by=10)

@app.route('/Users/<username>/') 
@login_required
def publication2(username):
    user=User.select().where(User.username==username).get()
    publications=Publication.select().where(Publication.user_created==user.id)
    return object_list('publications/list.html', publications, paginate_by=5)


@app.route('/publications/<int:id>')
@login_required
def publications_detail(id):
    publication = Publication.get(id)
    return render_template('publications/details.html', publication=publication)

@app.route('/User/login/',methods=['GET','POST', ])
@app.route('/User/login/<int:id>',methods=['GET','POST', ])
def users_login():
    user=User()
    form=LoginForm()
    if request.method== 'POST':
        try:
            user=User.select().where(User.username==request.form['username']).get()
        except:
            return render_template('users/login.html',form=form, user=user, error=1)
        
            
        if request.form['password']==user.password:
            session['id']=user.id
            session['username']=user.username
            login_user(user)
        else:
            return render_template('users/login.html',form=form, user=user, error=1)
                
        
        return redirect(url_for('publication'))
        
    else:
        return render_template('users/login.html',form=form, user=user)

                


@app.route('/User/register/', methods=['GET', 'POST', ])
@app.route('/User/register/<int:id>', methods=['GET', 'POST', ])

def users_register(id=None):
    if id:
        user = User.get(id)
    else:
        user = User()
    
    if request.method == 'POST':
        form = UserForm(request.form, obj=user) if id else UserForm(request.form)
        if form.validate():
            form.populate_obj(user)
            user.save()
            flash('You have been saved')
            return redirect(url_for('users_login'))
    else:
        form = UserForm(obj=user) if id else UserForm()
    return render_template('users/register.html', form=form, user=user)

@app.route('/users/list')
def liste_users():
    users=User.select()
    return render_template('users/list.html', users=users)


@app.route('/Publication/form/', methods=['GET', 'POST', ])
@app.route('/Publication/form/<int:id>', methods=['GET', 'POST', ])
@login_required
def publications_form(id=None):
    if id:
        publication = Publication.get(id)
    else:
        publication = Publication()
        publication.user_created=session["id"]
    
    if request.method == 'POST':
        form = PublicationForm(request.form, obj=publication) if id else PublicationForm(request.form)
        if form.validate():
            form.populate_obj(publication)
            publication.save()
            flash('Your publication has been saved')
            return redirect(url_for('publication'))
    else:
        form = PublicationForm(obj=publication) if id else PublicationForm()
    return render_template('publications/form.html', form=form, publication=publication)

@app.route('/Publication/delete/<int:id>')
def publication_delete(id=None):
    if id:
        try:
            publication=Publication.get(id)
        except:
            flash("error")
            return redirect(url_for('publication'))
        publication.delete_instance()
        flash("success")
    return redirect(url_for('publication'))


@app.route('/logout')
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('publication'))

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
    for user_ex in range(0, 5):
        user = User.create(username=fake.last_name(), password=fake.password(),first_name = fake.first_name(), last_name=fake.last_name(), email = fake.email())
        for publications_ex in range(0, 10):
            Publication.create(title = fake.sentence(), body = fake.text(),
                                      user_created=user)

@app.cli.command()
def testdb():
    for user in User.select():
        for publi in Publication.select():
            if publi.user_created == user:
                print(publi.user_created.id)

@app.cli.command()
def monuser():
    from faker import Faker
    fake = Faker()
    User.create(username='login', password='pass',first_name = fake.first_name(), last_name=fake.last_name(), email = fake.email())

@app.cli.command()
def test():
    username="login"
    user=User.select().where(User.username==username).get()
    publications= Publication.select().where(Publication.user_created==user.id)
    for publi in publications :
        print(publi)

