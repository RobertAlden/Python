from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *


def invoice_date_sub(dt1,dt2):
    diff = dt2 - dt1
    return (diff.seconds // 3600)

@app.template_filter()
def subtotal(wos):
    total = 0
    for w in wos:
        workorder = w[0]
        service = w[1]
        hours = invoice_date_sub(workorder.StartTime,workorder.EndTime)
        total += ((hours*service.HourCost + service.BaseCost)+(hours*workorder.PayRate))
    
    return "${:.2f}".format(total/100)           
                        


@app.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    if request.method == 'POST':
        owner_f_name = request.form['fname']
        owner_l_name = request.form['lname']
        owner_state = request.form['state']
        owner_city = request.form['city']
        owner_addr = request.form['addr']
        owner_zip = request.form['zip']
        owner_num = request.form['num']
        new_owner = Owner(FName=owner_f_name,
                          LName=owner_l_name,
                          State=owner_state,
                          City=owner_city,
                          StreetAddress=owner_addr,
                          Zip=int(owner_zip),
                          PhoneNum=owner_num)


        try:
            db.session.add(new_owner)
            db.session.commit()
            return redirect('/add_owner')
        except:
            return 'There was an issue adding a new owner'

    else:
        owners = Owner.query.order_by(Owner.LName).all()
        return render_template('features/owner/add_owner.html', owners=owners)


@app.route('/update_owner/<int:owner_id>', methods=['POST', 'GET'])
def update_owner(owner_id):
    owner_to_update = Owner.query.get_or_404(owner_id)

    if request.method == 'POST':
        owner_to_update.FName = request.form['fname']
        owner_to_update.LName = request.form['lname']
        owner_to_update.State = request.form['state']
        owner_to_update.City = request.form['city']
        owner_to_update.StreetAddress = request.form['addr']
        owner_to_update.Zip = request.form['zip']
        owner_to_update.PhoneNum = request.form['num']

        try:
            db.session.commit()
            return redirect('/add_owner')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('features/owner/update_owner.html',
                               owner=owner_to_update)


@app.route('/delete_owner/<int:owner_id>')
def delete_owner(owner_id):
    owner_to_delete = Owner.query.get_or_404(owner_id)

    try:
        Property.query.filter_by(OwnerID=owner_id).delete()
        db.session.delete(owner_to_delete)
        db.session.commit()
        return redirect('/add_owner')
    except:
        return 'There was a problem deleting that owner'


@app.route('/invoice/<int:owner_id>')
def invoice(owner_id):
    owner = Owner.query.get_or_404(owner_id)

    properties = Property.query.filter_by(OwnerID=owner_id)
    workorders = []
    for prop in properties:
        wos = db.session.query(WorkOrder,
                               Service,
                               Workman,
                               Property
                               ).filter_by(PropertyID=prop.PropertyID)\
                                .filter_by(IsComplete=True)\
                                .filter(Service.ServiceID == WorkOrder.ServiceID)\
                                .filter(Workman.WMID ==  WorkOrder.WMID)\
                                .filter(Property.PropertyID == WorkOrder.PropertyID)\
                                .order_by(WorkOrder.StartTime).all()
        workorders += wos
    return render_template('features/owner/invoice.html',
                           owner=owner, workorders=workorders)

if __name__ == "__main__":
    app.run(debug=True)