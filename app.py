import flask
import pickle

app=flask.Flask(__name__, template_folder='template')
@app.route('/',methods=['GET','POST'])
def main():
    if flask.request.method == 'POST':
        model=pickle.load(open('bin/model.pkl','rb'))
        gender=flask.request.form['gender']
        married=flask.request.form['married']
        dependents=flask.request.form['dependents']
        education=flask.request.form['education']
        employed=flask.request.form['employed']
        applicant_income=flask.request.form['applicant_income']
        coapplicant_income=flask.request.form['coapplicant_income']
        loan_amount=flask.request.form['loan_amount']
        loan_amount_term=flask.request.form['loan_amount_term']