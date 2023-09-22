from flask import Flask, request, render_template
from src.dbconnection import *
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        qry = "SELECT `question` FROM `datasets`"
        res = selectall(qry)
        lid = []
        for i in res:
            lid.append(i['question'])
        languages = ["C++", "Python", "PHP", "Java", "C", "Ruby",
                     "R", "C#", "Dart", "Fortran", "Pascal", "Javascript"]

        return render_template("auto.html", languages=lid)


if __name__ == '__main__':
    app.run(debug=True)
