# -*- coding: utf-8 -*-


import morepath


class App(morepath.App):
    pass


@App.path(path='')
class Root(object):
    pass


@App.view(model=Root)
def hello_world(self, request):
    return "Hello world!"


if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    morepath.run(App())
