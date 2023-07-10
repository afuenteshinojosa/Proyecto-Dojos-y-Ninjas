from flask import Flask

app = Flask(__name__)
app.secret_key = "shhh"

BASE_DATOS = "esquema_dojos_y_ninjas"


