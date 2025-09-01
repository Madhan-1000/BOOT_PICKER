from flask import Flask,render_template,request,jsonify
import json,os
app=Flask(__name__)

def load_data():
    json_file_path = os.path.join(app.static_folder, 'data', 'data.json')
    if not os.path.exists(json_file_path):
        return "Error: JSON file not found.", 404
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return "Error: Invalid JSON format.", 500
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500
        
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process_code", methods=["POST"])
def process_code():
    data = request.get_json()
    code = data.get("Input_code","")
    Result=parse_code(code)

    return jsonify({"extracted1":f"""{Result}"""})


def parse_code(html_content):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')
    classes = set()
    for tag in soup.find_all(class_=True):
        for class_name in tag.get('class', []):
            classes.add(f".{class_name}")
    return collect_css_code(list(classes))

def collect_css_code(classes):
    Data=load_data()
    Result=""""""
    ob="{"
    cl="}"
    for x in classes:
        if x in Data:
            Result+=f"""{x}{ob}
        {Data[x]} 
        {cl}\n"""
    return Result
if __name__=="__main__":
    app.run(debug=True,port=2000)