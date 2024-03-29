from models import Publication, User
from wtfpeewee.orm import model_form
from wtforms.validators import Length

PublicationForm= model_form(Publication, exclude=('created_date','update_date','user_created',))
UserForm= model_form(User,exclude=('created_at',))
LoginForm= model_form(User, exclude=('first_name','last_name','email','created_at',))