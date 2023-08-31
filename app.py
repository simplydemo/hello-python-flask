from flask import Flask, render_template, request, jsonify
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    name = request.args.get('name')
    if name is None:
        name = 'World'

    app.logger.info(f'request.name: {name}')

    return render_template('index.html', name=name)


@app.route("/echo", methods=["GET"])
def echo():
    url = request.url
    app.logger.info(f'request.url: {url}')

    req_json = request.get_json(force=False, silent=True)
    app.logger.info(f'request.json: {req_json}')

    return jsonify(
        {
            "url": url,
            "args": request.args,
            "data": request.data.decode("utf-8"),
            "form": request.form,
            "json": req_json,
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=False)
