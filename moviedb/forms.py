# forms.py

from wtforms import Form, StringField, SelectField

class MusicSearchForm(Form):
    choices = [('Released_Year', 'Released_Year'),
               ('Title', 'Title'),
               ('Director', 'Director'),
               ('Genre','Genre')]
    select = SelectField('Search for Movie/Series:', choices=choices)
    search = StringField('')
class AlbumForm(Form):
    media_types = [('Netflix', 'Netflix'),
                   ('Amazon Prime', 'Amazon Prime'),
                   ('SunNXT', 'SunNXT'),
                   ('123movies.com','123movies.com')
                   ]
    artist = StringField('Genre')
    title = StringField('Title')
    release_date = StringField('Released_Year')
    publisher = StringField('Director')
    media_type = SelectField('Available in', choices=media_types)