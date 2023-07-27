from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#secret key
app.config['SECRET_KEY']="damitaColombiana"
#initialize the database


#Create a Form Class
class NamerForm(FlaskForm):
    name=StringField("What's your name", validators =[DataRequired()])
    submit=SubmitField("Submit")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/<int:name>')
def user(name):
    return render_template("user.html", user=name)

@app.route('/name', methods=['GET','POST'])
def name():
    name=None
    form=NamerForm()
    #Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
        flash("Form Submitted Successfully!")
    return render_template("name.html", name=name, form=form)

#Invalid URL
@app.errorhandler(404)
def page_not_foundout(error):
    return render_template('errores/404.html'), 404
#Internal Server Error
@app.errorhandler(500)
def  page_not_found(error):
    return render_template('errores/504.html'), 500

if __name__ == '__main__':
    app.run(port=5559, debug=True)