
from flask import Flask, request, render_template,url_for,redirect

from sqlalchemy.exc import DataError,IntegrityError

from Create_tableSQL import *


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/information_user"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
db.init_app(app)

#____________________________________
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/SignIn")
def name_user():
    return render_template("SignIn.html")

@app.route("/library")
def library():
    return render_template("Mylibrary.html")

@app.route("/SignUp")
def sign_up():
    return render_template("SignUp.html")


@app.route("/introduce")
def introduce():
    return render_template("introduce.html")


@app.route('/error')
def error():
    return render_template('error.html')

@app.route("/find")
def find():
    return render_template("find.html")
#______________________________________
#Thông tin đăng ký mới 
@app.route("/signin")  
def signin():
    try:
   
        number_phone = request.args.get("phone")
        password = request.args.get("password")#request về password bên SignIn
        
        
        name_signin = Name_User(number_phone=number_phone, password=password) #pass ở đầu là var bên Create_tableSQL, pass còn lại là var bên này
        db.session.add(name_signin)  
        db.session.commit()

        return render_template("success.html")
    except IntegrityError:
        return redirect(url_for("error"))
    
    

#Đăng nhập vào web
@app.route("/login", methods=["GET","POST"]) #GET là yêu cầu dữ liệu từ bên sever thông qua URL của web/POST là gửi dữ liệu từ client lên sever  
                                              
def login():
    try:
        if request.method == "POST":
            number_phone = request.form.get("phone")
            password = request.form.get("password")
        
            user = Name_User.query.filter_by(number_phone=number_phone).first() #check tài khoản mật khẩu trong database
            if user and user.password == password:
                return redirect(url_for("library"))
            else:
                error = "Tài khoản hoặc mật khẩu không chính xác"
                return render_template("SignUp.html", error=error)
        else:
            return render_template("SignUp.html")
        
    except DataError:
        return redirect(url_for("sign_up")) #nhập chữ vào số điện thoại sẽ return về lại trang đăng nhập






















