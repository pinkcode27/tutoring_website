from app import app
from app import cli
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=False, threaded=True)
