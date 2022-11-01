from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *
from datetime import datetime, date, timedelta
from math import floor

@app.template_filter()
def date_iso(dt):
    return dt.isoformat()


@app.template_filter()
def date_sub(dt1,dt2):
    diff = dt2 - dt1
    return (diff.seconds // 3600)


@app.template_filter()
def longevity(dt):
    return floor((datetime.today() - dt).days / 365)


@app.template_filter()
def totalwage(ts):
    total = 0
    for t in ts:
        dur = date_sub(t.StartTime,t.EndTime)
        value = t.PayRate * dur
        total+=value
    return total



@app.route('/add_employee', methods=['POST', 'GET'])
def add_employee():
    if request.method == 'POST':
        emp_f_name = request.form['fname']
        emp_l_name = request.form['lname']
        emp_payrate = request.form['payrate']
        emp_hiredate = date.fromisoformat(request.form['hiredate'])
        emp_num = request.form['num']
        new_emp = Workman(FName=emp_f_name,
                          LName=emp_l_name,
                          PayRate=emp_payrate,
                          HireDate=emp_hiredate,
                          PhoneNum=emp_num)

        try:
            db.session.add(new_emp)
            db.session.commit()
            return redirect('/add_employee')
        except Exception as e:
            print(e)
            return 'There was an issue adding a new employee'

    else:
        employees = Workman.query.order_by(Workman.LName).all()
        return render_template('features/employee/add_employee.html',
                               employees=employees)

@app.route('/update_employee/<int:e_id>', methods=['POST', 'GET'])
def update_employee(e_id):
    wm_to_update = Workman.query.get_or_404(e_id)
    if request.method == 'POST':
        wm_to_update.FName = request.form['fname']
        wm_to_update.LName = request.form['lname']
        wm_to_update.PayRate = request.form['payrate']
        wm_to_update.HireDate = date.fromisoformat(request.form['hiredate'])
        wm_to_update.PhoneNum = request.form['num']

        try:
            db.session.commit()
            employees = Workman.query.order_by(Workman.LName).all()
            return render_template('features/employee/add_employee.html',
                                   employees=employees)
        except Exception as e:
            print(e)
            return 'There was an issue adding a new employee'

    else:
        return render_template('features/employee/update_employee.html',
                               employee=wm_to_update)

@app.route('/delete_employee/<int:wmid>')
def delete_employee(wmid):
    emp_to_delete = Workman.query.get_or_404(wmid)

    try:
        db.session.delete(emp_to_delete)
        db.session.commit()
        return redirect('/add_employee')
    except Exception as e:
        print(e)
        return 'There was an issue deleting that employee.'


@app.route('/view_timesheets/<int:wmid>', methods=['POST', 'GET'])
def view_timesheets(wmid):
    emp = Workman.query.get_or_404(wmid)
    if request.method == 'POST':
        timesheets = Timesheet.query.filter_by(WMID=wmid).order_by(Timesheet.StartTime).all()
        if request.form.get('startdate'):
            startdate = datetime.fromisoformat(request.form['startdate'])
            timesheets = [t for t in timesheets if t.StartTime >= startdate]
            
        if request.form.get('enddate'):
            enddate = datetime.fromisoformat(request.form['enddate'])
            timesheets = [t for t in timesheets if t.EndTime <= enddate]
        
    else:
        timesheets = Timesheet.query.filter_by(WMID=wmid).order_by(Timesheet.StartTime).all()

    return render_template('features/employee/view_timesheets.html',
                               employee=emp,timesheets=timesheets)


@app.route('/delete_timesheet/<int:tsid>')
def delete_timesheet(tsid):
    ts_to_delete = Timesheet.query.get_or_404(tsid)

    try:
        emp = Workman.query.get_or_404(ts_to_delete.WMID)
        db.session.delete(ts_to_delete)
        db.session.commit()
        timesheets = Timesheet.query.filter_by(WMID=emp.WMID).order_by(Timesheet.StartTime).all()
        return render_template('features/employee/view_timesheets.html',
                                employee=emp,timesheets=timesheets)
    except Exception as e:
        print(e)
        return "There was an issue deleting that timesheet."


if __name__ == "__main__":
    app.run(debug=True)
