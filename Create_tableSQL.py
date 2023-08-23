#Khởi tạo bảng
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/information_user"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class Name_User(db.Model):
    __tablename__ = "Information"
    number_phone = db.Column(db.Integer,primary_key=True) #số điện thoại là khóa chính
    password = db.Column(db.String, nullable=False)
    












     
    
     