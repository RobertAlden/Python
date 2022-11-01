from flask import Flask, render_template, url_for, request, redirect
from components.database.database import *


@app.route('/')
def index_page():
    owners = len(Owner.query.all())
    properties = len(Property.query.all())
    employees = len(Workman.query.all())
    return render_template('index.html', owners=owners,properties=properties,employees=employees)