from app import app
from app.models.db import dump_files, ANATHOMY


if __name__ == "__main__":
    dump_files(ANATHOMY.keys(), ANATHOMY)
    app.run(debug=True)