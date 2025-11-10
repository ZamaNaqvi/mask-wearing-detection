from flask import Flask, render_template

app = Flask(__name__)

#call the application root
@app.route('/')
def home():
    return render_template('index.html')

#to the main application on local sever 
if __name__ == '__main__':
    app.run(debug=True)