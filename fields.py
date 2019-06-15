from peewee import DateField as PeeweeDateField
from wtforms.fields.html5 import DateField as HTML5DateField


class DateField(PeeweeDateField):

    def wtf_field(self, model, **kwargs):
        return HTML5DateField(**kwargs)
