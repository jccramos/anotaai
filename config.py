import google.cloud.secretmanager  as secretmanager
import logging



logger = logging.getLogger()
logger.setLevel(logging.ERROR)

secrets = secretmanager.SecretManagerServiceClient()
PROJECT_ID = "anotaai-api"

GMAIL_AUTH_LOGIN = secrets.access_secret_version(
    request={"name": "projects/"+PROJECT_ID+"/secrets/gmail-auth-login/versions/1"}
).payload.data.decode("utf-8")


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
