from flask import Flask, render_template, request
from main import color_rank
from pprint import pprint
import time

app = Flask(__name__, template_folder="web\\templates", static_folder="web\\static")

@app.get("/")
def index_get():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def search():
    text = request.form["query"]

    start_time = time.time()
    results = color_rank(text)
    end_time = time.time()

    pprint(results)
    print("SEARCH QUERY:", text)
    print("About", (end_time - start_time), "seconds")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(port=8000)
