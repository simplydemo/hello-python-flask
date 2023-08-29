from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    name = request.args.get('name')
    if name is None:
        name = 'World'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
