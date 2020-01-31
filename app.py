from flask import Flask
from views.index import index_blueprint
from views.sample import sample_blueprint
from views.pages import pages_blueprint


app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(sample_blueprint)
app.register_blueprint(pages_blueprint, url_prefix='/pages')


if __name__ == '__main__':
    app.run(debug=True)
