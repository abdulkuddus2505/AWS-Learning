from application import create_app, db
from sqlalchemy.exc import OperationalError
import time

application = create_app()

with application.app_context():
    retry_count = 5
    for attempt in range(retry_count):
        try:
            db.create_all()
            break
        except OperationalError as e:
            print(f"[Attempt {attempt+1}] Database not ready: {e}")
            time.sleep(5)
