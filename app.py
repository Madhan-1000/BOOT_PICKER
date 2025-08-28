from flask import Flask,render_template,request,jsonify
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process_code", methods=["POST"])
def process_code():
    data = request.get_json()
    code = data.get("Input_code","")

    return jsonify({"extracted":f"{code}"})


def parse_code():
    pass

def collect_css_code():
    pass
if __name__=="__main__":
    app.run(debug=True,port=2000)