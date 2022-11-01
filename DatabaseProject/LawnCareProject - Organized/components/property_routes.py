from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *


@app.route('/add_prop/<int:owner_id>', methods=['POST', 'GET'])
def add_prop(owner_id):
    if request.method == 'POST':
        prop_state = request.form['state']
        prop_city = request.form['city']
        prop_addr = request.form['addr']
        prop_zip = request.form['zip']
        prop_desc = request.form['desc']
        new_prop = Property(State=prop_state,
                            City=prop_city,
                            StreetAddress=prop_addr,
                            Zip=prop_zip,
                            PropertyDesc=prop_desc,
                            OwnerID=owner_id)

        try:
            db.session.add(new_prop)
            db.session.commit()
            return view_props(owner_id)
        except:
            return 'There was an issue adding a new property'

    else:
        owner = Owner.query.get_or_404(owner_id)
        properties = Property.query.filter_by(OwnerID=owner_id).all()
        return render_template('features/property/add_property.html',
                               owner=owner, properties=properties)


@app.route('/update_prop/<int:owner_id>/<int:prop_id>', methods=['POST', 'GET'])
def update_prop(owner_id, prop_id):
    owner = Owner.query.get_or_404(owner_id)
    property_to_update = Property.query.get_or_404(prop_id)
    if request.method == 'POST':
        property_to_update.State = request.form['state']
        property_to_update.City = request.form['city']
        property_to_update.StreetAddress = request.form['addr']
        property_to_update.Zip = request.form['zip']
        property_to_update.PropertyDesc = request.form['desc']

        try:
            db.session.commit()
            return view_props(owner_id)
        except:
            return 'There was a problem updating that property'
    else:
        return render_template('features/property/update_property.html',
                               property=property_to_update,
                               owner=owner)

@app.route('/delete_prop/<int:owner_id>/<int:prop_id>')
def delete_prop(owner_id, prop_id):
    property_to_delete = Property.query.get_or_404(prop_id)

    try:
        db.session.delete(property_to_delete)
        db.session.commit()
        return view_props(owner_id)
    except:
        return 'There was a problem deleting that property'


@app.route('/prop_workorders/<int:owner_id>/<int:prop_id>')
def prop_workorders(owner_id,prop_id):
    owner = Owner.query.get_or_404(owner_id)
    prop = Property.query.get_or_404(prop_id)

    workorders = db.session.query(WorkOrder,
                               Service,
                               Workman,
                               Property
                               ).filter_by(PropertyID=prop.PropertyID)\
                                .filter(Service.ServiceID == WorkOrder.ServiceID)\
                                .filter(Workman.WMID ==  WorkOrder.WMID)\
                                .filter(Property.PropertyID == WorkOrder.PropertyID)\
                                .order_by(WorkOrder.StartTime).all()

    return render_template('features/property/property_workorders.html',
                           owner=owner, property=prop, workorders=workorders)

def view_props(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    properties = Property.query.filter_by(OwnerID=owner_id).all()
    return render_template('features/property/add_property.html',
                           owner=owner, properties=properties)


if __name__ == "__main__":
    app.run(debug=True)