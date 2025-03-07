from flask import Flask,request,render_templates

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    return(render_templates("index.html"))

if __name__ == "__main__":
    app.run()