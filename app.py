from flask import Flask, render_template, request
from file import topsis_func
from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import ssl
import smtplib
import os

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static/files'


email_sender = 'ridhimagupta0212@gmail.com'
email_password = os.environ.get('EMAIL_PASSWORD')


em = EmailMessage()
em['From'] = email_sender
em['Subject'] = 'Output of Topsis'
em.set_content(
    "This is the output result for your topsis.Thank you for using topsis generator.")

context = ssl.create_default_context()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getData():
    weight = request.form['weight']
    impact = request.form['impact']
    email = request.form['email']
    f = request.files['filename']
    f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

    file = "static/files/"+f.filename

    try:
        result_df = topsis_func(file, weight, impact)
        result_df.to_csv("static/files/result.csv")
    except:
        return "Error generated in topsis function"

    with open("static/files/result.csv", 'rb') as fp:
        file_data = fp.read()
    em.add_attachment(file_data, maintype='text',
                      subtype='csv', filename="result.csv")

    email_receiver = email
    em['To'] = email_receiver
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return "Email sent"


if __name__ == '__main__':
    app.run(debug=True)
