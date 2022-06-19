from flask import Flask, render_template, request, jsonify
from controller import *
import metrics

app = Flask(__name__)
setup()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/go")
def go():
    data = request.args.to_dict()
    for action in data.keys():
        print(action)
    return "OK"


@app.route("/get_metrics")
def metrics_data():
    return jsonify({"cpu_temp": metrics.get_temperature()})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

