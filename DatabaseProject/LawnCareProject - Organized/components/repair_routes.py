from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *
from datetime import datetime, date, timedelta


@app.route('/add_repair/<int:equip_id>', methods=['POST', 'GET'])
def add_repair(equip_id):
    if request.method == 'POST':
        repair_desc = request.form['desc']
        repair_date = date.fromisoformat(request.form['repairdate'])
        new_repair = Repair(RepairDesc=repair_desc,
                            RepairDate=repair_date,
                            EquipID=equip_id)

        try:
            db.session.add(new_repair)
            db.session.commit()
            return view_repairs(equip_id)
        except:
            return 'There was an issue adding a new repair'

    else:
        return view_repairs(equip_id)


@app.route('/delete_repair/<int:equip_id>/<int:repair_id>')
def delete_repair(equip_id,repair_id):
    repair_to_delete = Repair.query.get_or_404(repair_id)
    try:
        db.session.delete(repair_to_delete)
        db.session.commit()
        return view_repairs(equip_id)
    except:
        return "There was an issue deleting that repair."

def view_repairs(equip_id):
    equip = Equipment.query.get_or_404(equip_id)
    repairs = Repair.query.filter_by(EquipID=equip_id).order_by(Repair.RepairDate.desc()).all()
    return render_template('features/repair/add_repair.html',
                           equip=equip, repairs=repairs)