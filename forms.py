from models import Publication
from wtfpeewee.orm import model_form
from wtforms.validators import Length


"""DinosaurForm = model_form(Dinosaur, field_args={
    'name': dict(validators=[Length(min=3, max=200)],
                 label='Nom'),
})"""

PublicationForm= model_form(Publication, exclude=('created_date','update_date','user_created',))
