import google.cloud.secretmanager  as secretmanager

secrets = secretmanager.SecretManagerServiceClient()
PROJECT_ID = "anotaai-api"

GMAIL_AUTH_LOGIN = secrets.access_secret_version(
    request={"name": "projects/"+PROJECT_ID+"/secrets/gmail-auth-login/versions/1"}
).payload.data.decode("utf-8")
