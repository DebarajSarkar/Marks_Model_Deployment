#from marks import marks_prediciton
from flask import Flask , render_template, request
#mk=0
import marks as m

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def marks():
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediciton(hrs)
        #print(marks_pred)
        #mk = m.marks_prediciton(hrs)
        mk= marks_pred

    return render_template("index.html", my_marks = mk)


# @app.route("/sub", methods=['POST'])
# def submit():
#     #html->.py
#     if request.method == "POST":
#         name = request.form["username"]
    
#     #.py->html
#     return render_template("sub.html",n=name)


if __name__ == "__main__":
    app.run(debug=True)
