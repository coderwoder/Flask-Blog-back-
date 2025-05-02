from flaskblog import app
from flaskblog import db

if __name__=='__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
    