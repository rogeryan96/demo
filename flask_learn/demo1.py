from flask import Flask,abort
app = Flask(__name__)

@app.route('/')
def hello():
    abort(400)
    return 'Hello World!'

@app.errorhandler(400)
def error_400(obj):
    print dir(obj)
    print obj.get_headers()
    return "error 400"

if __name__ == '__main__':
    app.run()