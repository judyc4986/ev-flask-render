from flask import Flask, render_template, request

app = Flask(__name__)

# ================================
# MODEL FUNCTIONS
# ================================
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

# ================================
# ROUTES
# ================================
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ev_registrations", methods=["GET", "POST"])
def ev_registrations():
    # ALWAYS PASS DEFAULT VALUES
    result = None
    x_value = None

    if request.method == "POST":
        try:
            x_value = float(request.form["x"])
            result = ev_registrations_formula(x_value)
        except:
            result = "Invalid input."

    # ALWAYS pass BOTH variables to template
    return render_template(
        "ev_registrations.html",
        result=result,
        x_value=x_value
    )

@app.route("/adoption_rate", methods=["GET", "POST"])
def adoption_rate():
    # ALWAYS PASS DEFAULT VALUES
    result = None
    x_value = None

    if request.method == "POST":
        try:
            x_value = float(request.form["x"])
            result = adoption_rate_formula(x_value)
        except:
            result = "Invalid input."

    return render_template(
        "adoption_rate.html",
        result=result,
        x_value=x_value
    )

# ================================
# DEBUG LOCAL RUN
# ================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
