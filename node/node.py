from blockchain import Blockchain
import datetime

from flask import Flask, render_template, request, redirect, url_for

b = Blockchain()
b.create_block('Alice', 'TBC')
b.create_block('Bob', 'Diabetes')

app = Flask(__name__)

from wtforms import Form, StringField, validators

class MedicalRecordForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    description = StringField('Description', [validators.Length(min=1, max=200)])

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    form = MedicalRecordForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        description = form.description.data
        b.create_block(name, description)
        return redirect(url_for('blocks'))
    return render_template('index.html', form=form)

@app.route("/blocks")
def blocks():
    return render_template('blockchain.html', data=b.blocks)

if __name__ == "__main__":
    app.run()
