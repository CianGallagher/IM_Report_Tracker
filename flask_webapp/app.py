from datetime import date
from flask import Flask, render_template, jsonify, url_for, request, redirect
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
    return "Test report added successfully!"

@app.route('/submit_report', methods=['POST'])
def submit_report():
    report = Report(
        Investment_advisor_name=request.form['Investment_advisor_name'],
        fund_name=request.form['fund_name'],
        sub_fund_name=request.form['sub_fund_name'],
        delegate_name=request.form['delegate_name'],
        reporting_period=request.form['reporting_period'],
        report_date=date.today(),  
        status=request.form['status'],
        comments=request.form['comments']
    )
    db.session.add(report)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/api/reports', methods=['POST'])
def api_create_report():
    data = request.get_json()
    report = Report(
        Investment_advisor_name=data['Investment_advisor_name'],
        fund_name=data['fund_name'],
        sub_fund_name=data['sub_fund_name'],
        delegate_name=data['delegate_name'],
        reporting_period=data['reporting_period'],
        report_date=date.today(),
        status=data['status'],
        comments=data.get('comments', '')
    )
    db.session.add(report)
    db.session.commit()
    return jsonify({'message': 'created'}), 201

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

@app.route('/edit_report/<int:report_id>', methods=['GET', 'POST'])
def edit_report(report_id):
    report = Report.query.get_or_404(report_id)

    if request.method == 'POST':
        report.Investment_advisor_name = request.form['Investment_advisor_name']
        report.fund_name = request.form['fund_name']
        report.sub_fund_name = request.form['sub_fund_name']
        report.delegate_name = request.form['delegate_name']
        report.reporting_period = request.form['reporting_period']
        report.status = request.form['status']
        report.comments = request.form['comments']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_form.html', report=report)

@app.route('/delete_report/<int:report_id>', methods=['POST'])
def delete_report(report_id):
    report = Report.query.get_or_404(report_id)
    db.session.delete(report)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/ajax')
def ajax_page():
    return render_template('ajax.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
