from flask import Flask

app = Flask("meu App")

@app.route('/')
def hello():
    return "Hello Word"