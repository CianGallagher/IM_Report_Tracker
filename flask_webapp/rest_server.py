from datetime import date
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Investment_advisor_name = db.Column(db.String(100), nullable=False)
    fund_name = db.Column(db.String(100), nullable=False)
    sub_fund_name = db.Column(db.String(100), nullable=False)
    delegate_name = db.Column(db.String(100), nullable=False)
    reporting_period = db.Column(db.String(20), nullable=False)
    report_date = db.Column(db.Date, nullable=False, default=date.today)
    status = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.String(200), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
