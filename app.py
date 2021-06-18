
#import pyrebase 

from pyrebase import pyrebase
from flask import *
#
import model1
from datetime import datetime ,timedelta
#from pyrebase import initialize_app
#from Crypto.PublicKey import RSA




#from Crypto.PublicKey import RSA
app = Flask(__name__)
config =  {
    "apiKey": "AIzaSyBmSHK-a5CdoDjCWMmklbnBbRXu_8G4z_w",
    "authDomain": "test-9ea4a.firebaseapp.com",
  " projectId": "test-9ea4a",
    "storageBucket": "test-9ea4a.appspot.com",
   " messagingSenderId": "466741772248",
    "appId ": "1:466741772248:web:ae98ea45fd31b1b8cdfcad",
    "measurementId ": "G-0WR10BYN6G",
    "databaseURL" : ""
}
firebase =pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'POST' :
       email = request.form['name']
       password = request.form['Pass']
       auth.sign_in_with_email_and_password(email,password)
       return redirect("main.html")
    return render_template('login.html')   
@app.route('/main.html',methods=['GET','POST'])
def helloo():
    if request.method == 'POST' :
      #source = request.form['source']
      #to = request.form['destination'] 
      return redirect('output')
    return render_template( "main.html" )


@app.route('/output',methods=['GET','POST'])
def predict():
    if request.method == 'POST' :
      source = request.form['source']
      to = request.form['destination'] 
      date = int(request.form['inputdata'])
      #date1 = date + dt.timedelta(days=+1)
      b0=str(date)
      date0 = datetime.strptime(b0, '%Y%m%d')
      ans0=model1.prediction(date0)
      date0=date0.date()
      ans0=round(ans0,4)
      ans0=round(ans0,4)
      a1=date+1
      b1=str(a1)
      
      date1 = datetime.strptime(b1, '%Y%m%d')
      
      ans1=model1.prediction(date1)
      date1=date1.date()
      ans1=round(ans1,4)
      ans1=round(ans1,4)
      a2=date+2
      b2=str(a2)
      date2 = datetime.strptime(b2, '%Y%m%d')
      
      ans2=model1.prediction(date2)
      date2=date2.date()
      ans2=round(ans2,4)
      a3=date+3
      b3=str(a3)
      date3 = datetime.strptime(b3, '%Y%m%d')
      ans3=model1.prediction(date3)
      date3=date3.date()
      ans3=round(ans3,4)
      #val=model1.prediction()
      print(type(date))
      #print(type(date))
      #print('iam meenakshi')
    return render_template("output.html",x=source,y=to, d = date0 ,ans0=ans0 ,ans1=ans1,ans2=ans2,ans3=ans3, d1= date1,d2= date2,d3= date3)
    #return render_template( "main.html" )    
           
if __name__ == '__main__' :
  app.run(debug=True,port=5001)
