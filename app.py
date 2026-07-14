
from flask import Flask,render_template, request
from checkers import run_all_checks
from scorer import calculate_score
app=Flask(__name__)
@app.route("/")
def home():
   return render_template("index.html")
@app.route("/result",methods=["POST"])
def result():
   url = request.form["url"]
   results = run_all_checks(url)
   report = calculate_score(results)


   return render_template("result.html",url=url,score=report["score"],
                          verdict=report["verdict"],reasons=report["reasons"])
if __name__ == "__main__" :
  app.run(debug=True)