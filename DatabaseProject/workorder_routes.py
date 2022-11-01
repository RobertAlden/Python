from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *
from datetime import datetime, date, time, timedelta


@app.template_filter()
def date_sub(dt1,dt2):
    diff = dt2 - dt1
    return (diff.seconds // 3600)


@app.template_filter()
def time_iso(dt):
    return dt.time().isoformat()


@app.template_filter()
def is_late(dt):
    if date.today() + timedelta(days=1) > dt.date():
      return "(!)"
    else:
      return ""


@app.route('/add_workorder', methods=['POST', 'GET'])
def add_workorder():
    if request.method == "POST":
        if request.form.get('submit_button'):
            wo_scheduleddate = date.fromisoformat(request.form['scheduleddate'])
            wo_starttime = datetime.combine(wo_scheduleddate,
                                            time.fromisoformat
                                            (request.form['starttime']))
            wo_endtime = datetime.combine(wo_scheduleddate,
                                          time.fromisoformat
                                          (request.form['endtime']))
            wo_WMID = request.form['employee']
            wo_service = request.form['service']
            wo_property = request.form['property']
            wo_equip = request.form['equipment']
            wo_desc = request.form['desc']
            wm = Workman.query.get_or_404(wo_WMID)
            new_WO = WorkOrder(ScheduledDate=wo_scheduleddate,
                               WMID=wo_WMID,
                               ServiceID=wo_service,
                               PropertyID=wo_property,
                               OwnerID=1,
                               EquipID=wo_equip,
                               WODesc=wo_desc,
                               StartTime=wo_starttime,
                               EndTime=wo_endtime,
                               PayRate=wm.PayRate)
            try:
                db.session.add(new_WO)
                db.session.commit()
                return redirect('/add_workorder')
            except:
                return 'There was an issue adding this workorder'
        elif request.form.get('filter_button'):
            workorders = db.session.query(WorkOrder,
                                      Service,
                                      Workman,
                                      Property
                                      ).filter(Service.ServiceID == WorkOrder.ServiceID)\
                                       .filter(Workman.WMID ==  WorkOrder.WMID)\
                                       .filter(Property.PropertyID == WorkOrder.PropertyID)\
                                       .order_by(WorkOrder.StartTime).all()

            if request.form.get('startdate'):
                startdate = datetime.fromisoformat(request.form['startdate'])
                workorders = [w for w in workorders if w[0].StartTime >= startdate]
            
            if request.form.get('enddate'):
                enddate = datetime.fromisoformat(request.form['enddate'])
                workorders = [w for w in workorders if w[0].EndTime <= enddate]

            if request.form.get("complete") == "CHECKED":
                workorders = [w for w in workorders if not w[0].IsComplete]

            properties = Property.query.order_by(Property.OwnerID).all()
            services = Service.query.order_by(Service.ServiceDesc).all()
            equipment = Equipment.query.order_by(Equipment.EquipDesc).all()
            employees = Workman.query.order_by(Workman.LName).all()
            return render_template('features/workorder/add_workorder.html',
                                   workorders=workorders,
                                   properties=properties,
                                   services=services,
                                   equipment=equipment,
                                   employees=employees)
    else:
        workorders = db.session.query(WorkOrder,
                                      Service,
                                      Workman,
                                      Property
                                      ).filter(Service.ServiceID == WorkOrder.ServiceID)\
                                       .filter(Workman.WMID ==  WorkOrder.WMID)\
                                       .filter(Property.PropertyID == WorkOrder.PropertyID)\
                                       .order_by(WorkOrder.StartTime).all()

        properties = Property.query.order_by(Property.OwnerID).all()
        services = Service.query.order_by(Service.ServiceDesc).all()
        equipment = Equipment.query.order_by(Equipment.EquipDesc).all()
        employees = Workman.query.order_by(Workman.LName).all()
        return render_template('features/workorder/add_workorder.html',
                               workorders=workorders,
                               properties=properties,
                               services=services,
                               equipment=equipment,
                               employees=employees)


@app.route('/update_workorder/<int:wo_id>', methods=['POST', 'GET'])
def update_workorder(wo_id):
    wo_to_update = WorkOrder.query.get_or_404(wo_id)
    if request.method == 'POST':
        old_status = wo_to_update.IsComplete

        wo_to_update.ScheduledDate = date.fromisoformat(request.form['scheduleddate'])
        wo_to_update.StartTime = datetime.combine(wo_to_update.ScheduledDate,
                                        time.fromisoformat
                                        (request.form['starttime']))
        wo_to_update.EndTime = datetime.combine(wo_to_update.ScheduledDate,
                                      time.fromisoformat
                                      (request.form['endtime']))
        wo_to_update.WMID = request.form['employee']
        
        wo_to_update.IsComplete = request.form.get("complete") == "CHECKED"

        wo_to_update.ServiceID = request.form['service']
        wo_to_update.PropertyID = request.form['property']
        wo_to_update.EquipID = request.form['equipment']
        wo_to_update.WODesc = request.form['desc']
        wm = Workman.query.get_or_404(wo_to_update.WMID)
        wo_to_update.PayRate = wm.PayRate
        try:
            if old_status != wo_to_update.IsComplete and wo_to_update.IsComplete == True:
                wm = Workman.query.get_or_404(wo_to_update.WMID)
                new_TS = Timesheet(WMID=wo_to_update.WMID,
                                   StartTime=wo_to_update.StartTime,
                                   EndTime=wo_to_update.EndTime,
                                   PayRate=wm.PayRate)
                db.session.add(new_TS)
            db.session.commit()
            return redirect('/add_workorder')
        except:
            return 'There was an issue updating this workorder, no changes were made.'
    else:
        properties = Property.query.order_by(Property.OwnerID).all()
        services = Service.query.order_by(Service.ServiceDesc).all()
        equipment = Equipment.query.order_by(Equipment.EquipDesc).all()
        employees = Workman.query.order_by(Workman.LName).all()
        return render_template('features/workorder/update_workorder.html',
                        workorder=wo_to_update,
                        properties=properties,
                        services=services,
                        equipment=equipment,
                        employees=employees)


@app.route('/delete_workorder/<int:wo_id>')
def delete_workorder(wo_id):
    wo_to_delete = WorkOrder.query.get_or_404(wo_id)

    try:
        db.session.delete(wo_to_delete)
        db.session.commit()
        return redirect('/add_workorder')
    except:
        return 'There was an issue deleting that workorder'
