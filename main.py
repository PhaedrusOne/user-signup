from flask import Flask, request, redirect, render_template
import cgi
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html', title = "Sign Up")




@app.route("/validate", methods=["POST"])
def signup():
    username = request.form['username']  
    password = request.form['password']  
    verify = request.form['verify']  
    email = request.form['email']  

    username_val = ""  
    password_val = ""  
    verify_val = ""
    email_val = ""  

    if username == "":
        username_val = "Empty field"
    elif len(username) < 3 or len(username) > 20:
        username_val = "Username has to contain no less than 3 and not more than 20 characters"    
    elif " " in username:
        username_val = "Your username cannot contain any spaces."
         
    
    if password == "":
        password_val = "Empty field"
    elif len(password) < 3 or len(password) > 20:
        password_val = "Password cannot contain no less than 3 and no more than 20 characters"
    elif " " in password:
        password_val = "Your password cannot contain any spaces."
        
    
    if verify == "":
       verify_val = "Empty field"
    elif verify != password:
        verify_val = "Issue with verification. Try again"
        
    
    if email == "":
        pass   
    elif "@" not in email:
        email_val = "That is not a valid email address.Missing '@'"
    elif "." not in email:
        email_val = "That is not a valid email address.Missing '.'"
    elif " " in email:
        email_val = "Your Email cannot contain any space."
    elif len(email) < 3 or len(email) > 20:
        email_val = "Your email cannot contain no less than 3 and no more than 20 characters"

    
    if not username_val and not password_val and not verify_val and not email_val:  
        return render_template("Welcome.html", username=username)
    else:
        return render_template("index.html",username=username,
        username_val=username_val, password_val=password_val, verify_val=verify_val,email=email,email_val=email_val)

   

app.run()