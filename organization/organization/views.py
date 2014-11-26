# -*- coding: utf-8 -*-


from . import model
from .app import App


@App.json(model=model.Document)
def document_default(self, request):
    return {'id': self.id, 'title': self.title, 'content': self.content }
