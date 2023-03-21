import flask
import pickle

app=flask.Flask(__name__, template_folder='template')
@app.route('/',methods=['GET','POST'])
def main():
    if flask.request.method == 'POST':
        gender=float(flask.request.form['gender'])
        married=float(flask.request.form['married'])
        dependents=float(flask.request.form['dependents'])
        education=float(flask.request.form['education'])
        employed=float(flask.request.form['employed'])
        applicant_income=float(flask.request.form['applicant_income'])
        coapplicant_income=float(flask.request.form['coapplicant_income'])
        loan_amount=float(flask.request.form['loan_amount'])
        loan_amount_term=float(flask.request.form['loan_amount_term'])
        credit=float(flask.request.form['credit'])
        p_area=float(flask.request.form['p_area'])
        model=pickle.load(open('bin/model.pkl','rb'))
        return flask.render_template('index.html',loan_status=int(model.predict([[gender,married,dependents,education,employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit,p_area]])))
    else:
        return flask.render_template('index.html')