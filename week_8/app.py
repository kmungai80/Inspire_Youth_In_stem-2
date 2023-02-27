from flask import Flask
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

app.run(debug=True,port=8000)
 