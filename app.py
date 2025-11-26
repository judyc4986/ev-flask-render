
from flask import Flask, render_template, request

app = Flask(__name__)

def ev_registrations_formula(x: float) -> float:
    return (
        3773.495357 * x
        + -3.578990 * (x ** 2)
        + 0.002106 * (x ** 3)
    )

def adoption_rate_formula(x: float) -> float:
    return (
        0.000999 * x
        + -0.000001 * (x ** 2)
        + 0.000000 * (x ** 3)
    )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ev_registrations", methods=["GET", "POST"])
def ev_registrations():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            result = ev_registrations_formula(x)
        except:
            result = "Invalid input."
    return render_template("ev_registrations.html", result=result)

@app.route("/adoption_rate", methods=["GET", "POST"])
def adoption_rate():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            result = adoption_rate_formula(x)
        except:
            result = "Invalid input."
    return render_template("adoption_rate.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
