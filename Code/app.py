from flask import Flask, render_template

app = Flask(__name__)

####################################################

#Твой код

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/teach')
def teach():
	return render_template('teach.html')

####################################################

if __name__ == "__main__":
  app.run(debug=True)
