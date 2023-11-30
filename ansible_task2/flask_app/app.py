from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/projects')
def projects():
    return 'This is my Projects!'

@app.route('/blogs')
def blog():
    return 'Coming soon!'

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=9999)
