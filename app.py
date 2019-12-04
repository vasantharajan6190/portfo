from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("./index.html")

@app.route('/<string:page>')
def about(page):
	return render_template(page)

def write_to_file(data):
	with open("database.txt",mode="a") as database:
		email = data["email"]
		subject=data["subject"]
		message=data["message"]
		file = database.write(f"\n\n email:{email}\nsubject:{subject}\nMessage:{message}")

def write_to_csv(data):
	with open("database.csv",newline='',mode="a") as database2:
		email = data["email"]
		subject=data["subject"]
		message=data["message"]
		csvwriter = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow([email,subject,message])


@app.route('/submit', methods=['POST', 'GET'])
def login():
	if request.method=="POST":
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect("/thank.html")
	else:
		return "something went wrong"
	