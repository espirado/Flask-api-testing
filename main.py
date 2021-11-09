from flask import Flask,jsonify

app = Flask(__name__) 

@app.route("/")
def home():
    return "Hello "

@app.route("/health.json")
def health(): 
    return jsonify({"status": "up"}),200  

if __name__ == "__main__":
 app.run(host='0.0.0.0',port=7777,debug=True)