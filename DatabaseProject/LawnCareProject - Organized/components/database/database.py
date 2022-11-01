from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


class Owner(db.Model):
    OwnerID = db.Column(db.Integer, primary_key=True)
    FName = db.Column(db.String(25), nullable=False)
    LName = db.Column(db.String(25), nullable=False)
    State = db.Column(db.String(25), nullable=False)
    City = db.Column(db.String(25), nullable=False)
    StreetAddress = db.Column(db.String(25), nullable=False)
    Zip = db.Column(db.Integer, nullable=False)
    PhoneNum = db.Column(db.String(20), nullable=True)
    Properties = db.relationship('Property', backref='owner', lazy=True)

    def __repr__(self):
        return '<Owner %r>' % self.OwnerID


class Property(db.Model):
    PropertyID = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(25), nullable=False)
    City = db.Column(db.String(25), nullable=False)
    StreetAddress = db.Column(db.String(50), nullable=False)
    Zip = db.Column(db.Integer, nullable=False)
    PropertyDesc = db.Column(db.String(50), nullable=True)
    OwnerID = db.Column(db.Integer, db.ForeignKey('owner.OwnerID'),
                        nullable=False)
    WorkOrders = db.relationship('WorkOrder', backref='property', lazy=True)


class Workman(db.Model):
    WMID = db.Column(db.Integer, primary_key=True)
    FName = db.Column(db.String(25), nullable=False)
    LName = db.Column(db.String(25), nullable=False)
    PayRate = db.Column(db.Integer, nullable=False)  # in Cents Per Hour
    HireDate = db.Column(db.DateTime, default=datetime.utcnow)
    PhoneNum = db.Column(db.Integer, nullable=True)
    Experience = db.relationship('WorkExperience',
                                 backref='workman', lazy=True)
    Timesheets = db.relationship('Timesheet',
                                 backref='workman', lazy=True)
    WorkOrders = db.relationship('WorkOrder', backref='workman', lazy=True)


class WorkExperience(db.Model):
    SID = db.Column(db.Integer, primary_key=True)
    WMID = db.Column(db.Integer, db.ForeignKey('workman.WMID'),
                     primary_key=True)


class Service(db.Model):
    ServiceID = db.Column(db.Integer, primary_key=True)
    ServiceDesc = db.Column(db.String(50), nullable=False)
    BaseCost = db.Column(db.Integer, nullable=False)
    HourCost = db.Column(db.Integer, nullable=False)
    WorkOrders = db.relationship('WorkOrder', backref='service', lazy=True)


class Equipment(db.Model):
    EquipID = db.Column(db.Integer, primary_key=True)
    EquipDesc = db.Column(db.String(50), nullable=False)
    ServicePeriod = db.Column(db.Integer, nullable=False)
    DateLastServiced = db.Column(db.DateTime, default=datetime.utcnow)
    Repair = db.relationship('Repair', backref='equipment', lazy=True)
    WorkOrders = db.relationship('WorkOrder', backref='equipment', lazy=True)


class Repair(db.Model):
    RepairID = db.Column(db.Integer, primary_key=True)
    EquipID = db.Column(db.Integer, db.ForeignKey('equipment.EquipID'))
    RepairDesc = db.Column(db.String(50), nullable=False)
    RepairDate = db.Column(db.DateTime, default=datetime.utcnow)


class Timesheet(db.Model):
    TSID = db.Column(db.Integer, primary_key=True)
    WMID = db.Column(db.Integer, db.ForeignKey('workman.WMID'))
    StartTime = db.Column(db.DateTime, default=datetime.utcnow)
    EndTime = db.Column(db.DateTime, default=datetime.utcnow)
    PayRate = db.Column(db.Integer, nullable=False)  # in Cents Per Hour


class WorkOrder(db.Model):
    WOID = db.Column(db.Integer, primary_key=True)
    ScheduledDate = db.Column(db.DateTime, default=datetime.utcnow)
    WMID = db.Column(db.Integer, db.ForeignKey('workman.WMID'))
    PayRate = db.Column(db.Integer, nullable=True)  # in Cents Per Hour
    ServiceID = db.Column(db.Integer, db.ForeignKey('service.ServiceID'))
    PropertyID = db.Column(db.Integer, db.ForeignKey('property.PropertyID'))
    OwnerID = db.Column(db.Integer, db.ForeignKey('owner.OwnerID'))
    EquipID = db.Column(db.Integer, db.ForeignKey('equipment.EquipID'))
    IsComplete = db.Column(db.Boolean, default=False)
    WODesc = db.Column(db.String(200), nullable=True)
    StartTime = db.Column(db.DateTime, default=datetime.utcnow)
    EndTime = db.Column(db.DateTime, default=datetime.utcnow)


if __name__ == "__main__":
    print("Database initalized")
    db.create_all()
