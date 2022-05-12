from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page>')
def load_page(page):
    return render_template(page)

def write_to_csv(new_data):
    email=new_data["email"]
    subject=new_data["subject"]
    message=new_data["message"]
    data_file = open("database.csv", "a", newline="")
    csv.writer(data_file,delimiter=";").writerow([email,subject,message])
    data_file.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect("/thanks.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong. try again."

