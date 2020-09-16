from myflaskproj import app

@app.route('/')
def hello():
    return '<h1>Welcome to MyFlaskProj </h1>'    