from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    msg = 'Hello'
    return render_template('index.html', message=msg)


@app.route('/', methods=['POST'])
def output():
    name = request.form['name']
    age = request.form['age']
    msg = "%s %s歳" % (name, age)
    return render_template('index.html', message=msg)


if __name__ == "__main__":
    app.run(debug=True)
