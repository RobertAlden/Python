from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *
from datetime import datetime, date, timedelta

@app.template_filter()
def dt_delta(dt,input_days):
    return dt + timedelta(days=input_days)


@app.template_filter()
def is_late(dt):
    if date.today() + timedelta(days=1) > dt.date():
      return "(!)"
    else:
      return ""


@app.route('/add_equip', methods=['POST', 'GET'])
def add_equipment():
    if request.method == 'POST':
        equip_desc = request.form['desc']
        equip_lastservicedate = date.fromisoformat(request.form['lastserviceddate'])
        equip_serviceperiod = request.form['period']
        new_equip = Equipment(EquipDesc=equip_desc,
                              DateLastServiced=equip_lastservicedate,
                              ServicePeriod=equip_serviceperiod)

        try:
            db.session.add(new_equip)
            db.session.commit()
            return redirect('/add_equip')
        except:
            return 'There was an issue adding a new piece of equipment'

    else:
        equipment = Equipment.query.all()
        return render_template('features/equipment/add_equipment.html',
                               equipment=equipment)


@app.route('/update_equip/<int:eq_id>', methods=['POST', 'GET'])
def update_equipment(eq_id):
    equip_to_update = Equipment.query.get_or_404(eq_id)
    if request.method == 'POST':
        equip_to_update.EquipDesc = request.form['desc']
        equip_to_update.DateLastServiced = date.fromisoformat(request.form['lastserviceddate'])
        equip_to_update.ServicePeriod = request.form['period']

        try:
            db.session.commit()
            return redirect('/add_equip')
        except:
            return 'There was an issue adding a new piece of equipment'

    else:
        equipment = Equipment.query.all()
        return render_template('features/equipment/update_equipment.html',
                               equip=equip_to_update)


@app.route('/delete_equip/<int:equip_id>')
def delete_equip(equip_id):
    equip_to_delete = Equipment.query.get_or_404(equip_id)

    try:
        db.session.delete(equip_to_delete)
        db.session.commit()
        return redirect('/add_equip')
    except:
        return 'There was an issue deleting that piece of equipment'


@app.route('/equip_workorders/<int:equip_id>')
def equip_workorders(equip_id):
    equip = Equipment.query.get_or_404(equip_id)

    workorders = db.session.query(WorkOrder,
                               Service,
                               Workman,
                               Property
                               ).filter_by(EquipID=equip.EquipID)\
                                .filter(Service.ServiceID == WorkOrder.ServiceID)\
                                .filter(Workman.WMID ==  WorkOrder.WMID)\
                                .filter(Property.PropertyID == WorkOrder.PropertyID)\
                                .order_by(WorkOrder.StartTime).all()

    return render_template('features/equipment/equipment_workorders.html',
                           equip=equip, workorders=workorders)


if __name__ == "__main__":
    app.run(debug=True)