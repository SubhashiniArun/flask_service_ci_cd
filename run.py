import threading

from app import create_app
from worker import start_worker

import logging

logging.basicConfig(level=logging.INFO)

app = create_app(config_name="development")

if __name__ == "__main__":
    threading.Thread(target=start_worker, daemon=True).start()
    app.run(host="0.0.0.0", port=5001, debug=True)