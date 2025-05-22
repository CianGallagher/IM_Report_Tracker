from datetime import date
from flask import Flask, render_template, jsonify
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
    reports = Report.query.all()
    return render_template('index.html', reports=reports)

@app.route('/test_report')
def add_test_report():
    sample_report = Report(
        Investment_advisor_name="Big Company",
        fund_name="Big Company Pension Fund",
        sub_fund_name="Emerging Markets Equity",
        delegate_name="State Street",
        reporting_period="Q1 2025",
        status="Received",
        comments="Report received on time per SLA",
    )
    db.session.add(sample_report)
    db.session.commit()
    return "Test report added!"

@app.route('/submit_report')
def submit_report():
    report = Report(
        Investment_advisor_name="Test IA",
        fund_name="Test Fund",
        sub_fund_name="Test Sub-Fund",
        delegate_name="Test Delegate",
        reporting_period="Q1 2025",
        report_date=date.today(),
        status="Pending",
        comments="Test entry"
    )
    db.session.add(report)
    db.session.commit()
    return "Basic test report submitted"

@app.route('/api/reports', methods=['GET'])
def return_json_reports():
    reports = Report.query.all()
    return jsonify([
        {
            'id': report.id,
            'investment_advisor_name': report.Investment_advisor_name,
            'fund_name': report.fund_name,
            'sub_fund_name': report.sub_fund_name,
            'delegate_name': report.delegate_name,
            'reporting_period': report.reporting_period,
            'report_date': report.report_date.strftime('%Y-%m-%d'),
            'status': report.status,
            'comments': report.comments
        } for report in reports
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
