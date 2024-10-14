from flask import Flask
from routes import api  # Import the blueprint containing routes
from middleware import authenticate_token  

app = Flask(__name__)


app.register_blueprint(api, url_prefix='/api')


@app.before_request
def before_request_func():
    auth_response = authenticate_token()  
    if auth_response:  
        return auth_response

if __name__ == '__main__':
    app.run(debug=True)
