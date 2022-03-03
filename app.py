from flask import Flask, render_template, request,url_for, flash
from pickle import load



app=Flask(__name__)
app.secret_key= "mykey"
model = load(open('RF_regression_mdl.pkl','rb'))

# the route can be either requested with a '/' or '/Equity-Predictions'
@app.route("/Equity-Predictions", methods=["POST","GET"])
@app.route("/", methods=["POST","GET"])
def equity_predictions():
    if request.method == 'POST':
        try:
            hp = float(request.form.get('high_price'))
            lp = float(request.form.get('low_price'))
            ltp = float(request.form.get('last_traded_price'))
            cp = float(request.form.get('close_price'))
            ttq = float(request.form.get('total_traded_quantity'))
            to = float(request.form.get('turnover'))
            pred = model.predict([[ hp, lp, ltp, cp, ttq, to ]])
            prediction = round(pred[0],2)
            return render_template("equity_prediction.html", open_price = "Open price is predicted to be : {}".format(prediction))
        except:
            flash('Please enter correct values')
    return render_template("equity_prediction.html")


if __name__=="__main__":
    app.run(debug=True)