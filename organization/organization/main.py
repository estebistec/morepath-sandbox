# -*- coding: utf-8 -*-


import morepath
from werkzeug.serving import run_simple

from .app import App


def main():
    # morepath.autosetup()
    config = morepath.setup()
    config.scan()
    config.commit()
    # morepath.run(App())
    run_simple('localhost', 5000, App(), use_reloader=True)
