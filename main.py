from pathlib import Path
from app import app
import views

if __name__ == '__main__':
    app.run(
	  host='0.0.0.0',
	  debug=True,
	  port=8080
    )