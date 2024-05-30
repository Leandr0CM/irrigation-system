from controllers.app_controller import create_app
from utils.create_db import create_db
#from flask_login import LoginManager


if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(host='0.0.0.0', debug=False)