from app import create_app
from app.seed import customer
from app.seed import video
from dotenv import load_dotenv

load_dotenv()

with create_app().app_context():
    customer.load()
    video.load()