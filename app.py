import os

from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin

from crawler import create_xlsx_file
from utils import parse_request, mk_massage
from config import GMAIL_AUTH_LOGIN, ERRORS, logger


app = Flask(__name__)
CORS(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'equipeanotaai@gmail.com'
app.config['MAIL_PASSWORD'] = GMAIL_AUTH_LOGIN.replace("[", "").replace("]","")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/anotai', methods=['POST'])
@cross_origin()
def welcome():
    if request.method == "POST":
        try:
            url, email, premium_user = parse_request(request)
            item, local = create_xlsx_file(url)
            msg = mk_massage(Message, local, premium_user, email, app)
            mail.send(msg)
            os.remove("detalhes_compra.xlsx")
        except Exception as e:
            logger.error(f"Error in Welcome: {e}")
            return ERRORS["invalid_link"]
        return item.values.tolist()
    else:
        return ""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
