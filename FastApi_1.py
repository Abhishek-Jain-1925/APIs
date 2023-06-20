from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def sayHello():
    return "Hello World...!!  Jay Jinendra...!! from @Abhishek Jain."

@app.get("/name")
def index(name:str):
    string = "Hello GentleMan...!! Welocme {0} in Jainism World..!!".format(name)
    return string

@app.get("/Addition/Numbers")
def sum(num1:int,num2:int):
    result = num1+num2
    str = "Addition of {0} and {1} = {2}".format(num1,num2,result)
    return str

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=1008)