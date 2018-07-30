from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/myresume')
def myresume():
    return app.send_static_file('myresume.html')

@app.route('/3d')
def get3d():
    return app.send_static_file('Renderer/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)