## MORE CODE ABOVE

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=request.form.get('password')
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("secrets"))

    return render_template("register.html")

## MORE CODE BELOW