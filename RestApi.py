from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/',methods=['POST'])
def home():
    str1="Welcome Home !! @Abhishek Jain"
    return str1

@app.route('/xyz',methods=['POST'])
def test1():
    a = request.json['num1']
    b = request.json['num2']
    #Here,Input Data Fetched from Postman to Test Given Rest API.
    #So, for this Rest API You Need Postman for Testing.
    result = a+b
    return jsonify(str(result))

@app.route('/hello',methods=['POST'])
def hello():
    if request.method=="POST":
        str = "Hello World...!! This is Abhishek Jain from Fergusson College,Pune."
        return str

if __name__ == '__main__':
    app.run()