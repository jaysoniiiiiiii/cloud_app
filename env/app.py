from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.app_context().push()

db = SQLAlchemy(app)

class account_info(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(200))
    email =  db.Column(db.String(200))
    access_key =  db.Column(db.String(200), nullable = False)
    secrete_access_key =  db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Task %r>' % self.id
    
def demo():
    return "hi jay this is running"

@app.route('/')

def __init__():
    
    return render_template("index.html")

@app.route('/form_login', methods = ['POST','GET'])  #'GET'
def logged():
    user_name = request.form['name']
    user_email = request.form['email']
    user_access_key = request.form['access_key']
    user_secrete_access_key = request.form['secrete_access_key']

    new_user = account_info(name = user_name, email = user_email, access_key = user_access_key, secrete_access_key =  user_secrete_access_key)
    db.session.add(new_user)
    db.session.commit()
                                                                                                                                    # user_email = request.form['email']
                                                                                                                                    # new_email = account_info(email = user_email)
                                                                                                                                    # db.session.add(new_email)
                                                                                                                                    # db.session.commit()
    task = account_info.query.filter_by(name = user_name,  email = user_email, access_key = user_access_key, secrete_access_key =  user_secrete_access_key)
    print(new_user, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(account_info, "0000000>>>>>>>>000000000")
    demo()
    return render_template("main.html", tasks = task)
















































    #         db.session.commit()
    #         task = Todo.query.first()

    #         return redirect("main.html")
    # if request.method == 'POST':
    #     user_name = request.form['name']
    #     new_name = Todo(name = user_name)

    #     try:
    #         db.session.add(new_name)
    #         db.session.commit()
    #         task = Todo.query.first()

    #         return redirect("main.html")

    #     except:
    #         cred = Todo.query.all()

    #         return redirect("main.html")
    #         # return "#####"
    # else:
    #     cred = Todo.query.all()

    #     return render_template("index.html")



if __name__ == "__main__":
    app.run(debug= True)