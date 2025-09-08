from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "home route"

#api endpoint
@app.route("/test",methods=["post"]) 
def about():
    data = request.json
    print(data)
    return "about route abcd"

@app.route("/update",methods=["put"])
def updatenote():
    return "note update Success"

@app.route("/delete",methods=["delete"])
def deletenote():
    return "notes are delete successfully"
app.run(debug=True)    

