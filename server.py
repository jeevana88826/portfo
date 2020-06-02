from flask import Flask,render_template
from flask import request,redirect
import csv

app=Flask(__name__)

@app.route('/')

def my_home():
    
    return render_template("index.html")


@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)
def write_to_csv(data):
    with open("database.csv",mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=",")
        csv_writer.writerow([email,subject,message])
def write_to_file(data):
    with open("database.txt",mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form',methods=["GET","POST"])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        write_to_file(data)
        #print(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong ,Please try again later"


#@app.route('/index.html')

#def my_home_1():
#   return render_template("index.html")
#@app.route('/works.html')
#def my_works():
#   return render_template("works.html")


#@app.route('/about.html')
#def my_about():
#   return render_template("about.html")

#@app.route('/contact.html')
#def my_contact():
#   return render_template("contact.html")





