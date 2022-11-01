from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *


@app.route('/add_service', methods=['POST', 'GET'])
def add_service():
    if request.method == 'POST':
        service_desc = request.form['desc']
        service_bcost = request.form['basecost']
        service_hcost = request.form['hourcost']
        new_service = Service(ServiceDesc=service_desc,
                              BaseCost=service_bcost,
                              HourCost=service_hcost)
        try:
            db.session.add(new_service)
            db.session.commit()
            return redirect('/add_service')
        except:
            return 'There was an issue adding a new service'

    else:
        services = Service.query.order_by(Service.ServiceDesc).all()
        return render_template('features/service/add_service.html', services=services)


@app.route('/update_service/<int:service_id>', methods=['POST', 'GET'])
def update_service(service_id):
    service_to_update = Service.query.get_or_404(service_id)

    if request.method == 'POST':
        service_to_update.ServiceDesc = request.form['desc']
        service_to_update.BaseCost = request.form['basecost']
        service_to_update.HourCost = request.form['hourcost']

        try:
            db.session.commit()
            return redirect('/add_service')
        except:
            return 'There was an issue updating that service'
    else:
        return render_template('features/service/update_service.html',
                               service=service_to_update)


@app.route('/delete_service/<int:service_id>')
def delete_service(service_id):
    service_to_delete = Service.query.get_or_404(service_id)

    try:
        db.session.delete(service_to_delete)
        db.session.commit()
        return redirect('/add_service')
    except:
        return 'There was a problem deleting that service'


if __name__ == "__main__":
    app.run(debug=True)