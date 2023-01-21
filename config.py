import google.cloud.secretmanager  as secretmanager
import logging



logger = logging.getLogger()
logger.setLevel(logging.ERROR)

secrets = secretmanager.SecretManagerServiceClient()
PROJECT_ID = "anotaai-api"

GMAIL_AUTH_LOGIN = secrets.access_secret_version(
    request={"name": "projects/"+PROJECT_ID+"/secrets/gmail-auth-login/versions/1"}
).payload.data.decode("utf-8")

db_pass = secrets.access_secret_version(
    request={"name": "projects/"+PROJECT_ID+"/secrets/db-dev-pass/versions/1"}
).payload.data.decode("utf-8")
instance_connection_name = secrets.access_secret_version(
    request={"name": "projects/"+PROJECT_ID+"/secrets/instance-connection-name/versions/1"}
).payload.data.decode("utf-8")
db_user = "dev-user"
db_name = "anotaai-bd"


ERRORS = {
    "invalid_link": [
        [
            "Desculpe, o link inserido a partir do QR-code lido é inválido",
            "error",
            "", #não usa
            "Desculpe, o link inserido a partir do QR-code lido é inválido",
            "",
            0.0,
            0.0
        ]
    ]
}
