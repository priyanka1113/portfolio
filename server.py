from flask import Flask,render_template,url_for,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

# @app.route('/works.html')
# def work():
# 	return render_template('works.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# app=Flask(__name__)
# print(__name__)

# @app.route('/')
# def home():
# 	print(url_for('static', filename='favicon_io/favicon.ico'))
# 	return render_template('index.html')


# @app.route('/blog')
# def blog():
# 	return "This is my blog"

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)



def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file= database.write(f'\n{email},{subject},{message}')



def write_to_csv(data):
	with open('database.csv',mode='a') as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_file= csv.writer(database2,delimiter=',',newline='',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method=='POST':
		#try:
			data=request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		#except:
		#	return "did not save to database"	
	else:
		return 'something went wrong please try again!'
# @app.route('/blog/2023/dogs')
# def blog_2023():
# 	return "this is blog for dogs in 2023"


