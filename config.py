import os
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEBUG = bool(int(os.getenv('DEBUG')))
WEBHOOK_SCHEMA = os.getenv("WEBHOOK_SCHEMA")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
WEBHOOK_PORT = os.getenv("WEBHOOK_PORT")
WEBHOOK_URL = f"{WEBHOOK_SCHEMA}://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
WEBAPP_HOST = os.getenv("WEBAPP_HOST")
WEBAPP_PORT = os.getenv("WEBAPP_PORT")
