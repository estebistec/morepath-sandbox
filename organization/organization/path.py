# -*- coding: utf-8 -*-


from . import model
from .app import App


@App.path(model=model.Document, path='/documents/{id}')
def get_document(id):
    if id != 'foo':
        return None  # not found
    return model.Document('foo', 'Foo document', 'FOO!')
