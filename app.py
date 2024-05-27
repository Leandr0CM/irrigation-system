from controllers.app_controller import create_app
from utils.create_db import create_db

if __name__ == "__main__":
    #cria o aplicativo e o db
    app = create_app()
    create_db(app)
    app.run(host='0.0.0.0', debug=False)