# -*- coding: utf-8 -*-


from webob.exc import HTTPNotAcceptable
import morepath


class App(morepath.App):
    pass


class User(object):
    def __init__(self, username, fullname, email):
        self.username = username
        self.fullname = fullname
        self.email = email


users = {}
def add_user(user):
    users[user.username] = user

faassen = User('faassen', 'Martijn Faassen', 'faassen@startifact.com')
bob = User('bob', 'Bob Bobsled', 'bob@example.com')
add_user(faassen)
add_user(bob)


@App.path(model=User, path='/users/{username}')
def get_user(username):
    return users.get(username)


@App.view(model=User)
def user_info(self, request):
    return "User's full name is: %s" % self.fullname


@App.json(model=User, name='info')
def user_json_info(self, request):
    return {
        'username': self.username,
        'fullname': self.fullname,
        'email': self.email
    }


@App.html(model=User)
def user_info(self, request):
    return "<p>User's full name is: %s</p>" % self.fullname


@App.view(model=User, name='extra')
def redirecting(self, request):
    return morepath.redirect(request.link(self, 'other'))


# @App.view(model=User, name='extra')
# def erroring(self, request):
#     raise HTTPNotAcceptable()


if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    morepath.run(App())
