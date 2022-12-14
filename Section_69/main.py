## MORE CODE ABOVE

#Import RegisterForm from forms.py
from forms import CreatePostForm, RegisterForm

#Create the User Table
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    
# Create all the tables in the database
db.create_all()
  

#Register new users into the User database
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=form)
  
  ## MORE CODE BELOW