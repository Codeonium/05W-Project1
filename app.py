from flask import Flask, render_template

from controllers.keikos_controller import keikos_blueprint
from controllers.senseis_controller import senseis_blueprint
from controllers.deshis_controller import deshis_blueprint
from controllers.wazas_controller import wazas_blueprint


app = Flask(__name__)


app.register_blueprint(keikos_blueprint)
app.register_blueprint(senseis_blueprint)
app.register_blueprint(deshis_blueprint)
app.register_blueprint(wazas_blueprint)


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()