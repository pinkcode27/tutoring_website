from app import app
from app import cli
import logging

cli.regsiter(app)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True, threaded=True)
