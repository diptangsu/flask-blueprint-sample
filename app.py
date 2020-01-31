from flask import Flask
from views.index import index_blueprint
from views.sample import sample_blueprint


app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(sample_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
