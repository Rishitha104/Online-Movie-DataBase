from flask_table import Table, Col,LinkCol

class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Genre')
    title = Col('Title')
    release_date = Col('Released_Year')
    publisher = Col('Director')
    media_type = Col('Available in')
    
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))