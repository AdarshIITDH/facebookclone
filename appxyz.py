from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellowworld():
    return 'Hello World'

if __name__=="main":
    app.run(port=3000,debug=True)
