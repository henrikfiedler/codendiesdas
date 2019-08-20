from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/test')
def test():
    return '<h1>Dies ist ein Test<h1>'

@app.route('/calculator')
def calculator():
    return render_template("h_calculator.html")

@app.route('/calc', methods=['post'])
def calc():
    zahl1 = request.form['zahl1']
    zahl2 = request.form['zahl2']
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)
    submit = request.form['submit']

    if submit == "Plus":
        erg = zahl1 + zahl2
    elif submit == "Minus":
        erg = zahl1 - zahl2
    elif submit == "Mal":
        erg = zahl1 * zahl2
    elif submit == "Geteilt":
        erg = zahl1 / zahl2
    
    return render_template("h_calc.html", ergebnis=erg)
    


if __name__ == '__main__':
    app.run(debug=True)