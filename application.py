from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home_pg():

    return render_template('index.html')

@app.route("/share",methods=['GET','POST'])
def share():
	


    
    return render_template('share.html')


@app.route("/courses",methods=['GET','POST'])
def courses():
    
    return render_template('course.html')

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)
