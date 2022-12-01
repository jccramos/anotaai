import os
import logging

from flask import Flask, request
from flask_mail import Mail, Message
from crawler import main
from utils import get_subject_elements, compose_msg
from config import GMAIL_AUTH_LOGIN, ERRORS


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'equipeanotaai@gmail.com'
app.config['MAIL_PASSWORD'] = GMAIL_AUTH_LOGIN.replace("[", "").replace("]","")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

@app.route('/anotai', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
        post_request = request.get_json(force=True)
        url = post_request["url"]
        email = post_request["email"]
        premium_user=post_request["premium"]

        item, local = main(url)
        try:
            item.to_excel(
                f"detalhes_compra.xlsx",
                index=False
            )
        except:
            logger.error(f"""
                An AttributeError ocurred for {email},
                this probably happened due to some problem with the URL passed in the request body.
                the URL used was {url}
            """)
            return ERRORS["invalid_link"]

        msg_local, msg_day, msg_when = get_subject_elements(local)
        if premium_user:
            msg = Message(
                f"Gastos em {msg_local} {email}",
                sender ='equipeanotaai@gmail.com',
                recipients=['equipeanotaai@gmail.com']
            )
        else:
            msg = Message(
                f"Gastos em {msg_local}",
                sender ='equipeanotaai@gmail.com',
                recipients=[email]
            )

        msg.html = compose_msg(msg_local, msg_day, msg_when)

        with app.open_resource("detalhes_compra.xlsx") as fp:
            if premium_user:
                msg.attach(f"detalhes_compra_{email}.xlsx", "detalhes_compra/xlsx", fp.read())
            else:
                msg.attach(f"detalhes_compra.xlsx", "detalhes_compra/xlsx", fp.read())

        mail.send(msg)
        os.remove("detalhes_compra.xlsx")

        # TODO: Wait the implementation in mobile to return this one!
        #local_item =local.to_json)
        return item.values.tolist()
    else:
        return "The request method was unexpected!!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
