from bottle import run, route

@route('/')
def index():
    return '<h1> Hello , world</h1>'

if __name__ == '__main__':
    run()
#modified