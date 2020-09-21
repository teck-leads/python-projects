from flask import Flask, make_response, request

app = Flask(__name__)


# use the route '/setcookie/' to set cookie

@app.route('/setcookie/')
def setcookie():
    resp = make_response("cookie was successfully set")
    resp.set_cookie('usercount', max_age=0)
    return resp



# use the route '/getcookie/' to get cookie
@app.route('/getcookie/')
def getcookie():
    count = int(request.cookies.get('usercount',0))
    count += 1
    message = 'you visited this site '+ str(count) + ' times'
    resp = make_response(message)
    resp.set_cookie('usercount', str(count))
    return resp

@app.route('/')
def testApp():
   
    return "Test app"

if __name__ == '__main__':  
    app.run(debug = True)  