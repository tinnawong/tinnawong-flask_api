from app import app
from dotenv import load_dotenv
import os

load_dotenv('.env')
host = os.environ.get("FLASK_RUN_HOST")
port = os.environ.get("FLASK_RUN_PORT")

if host !="" and port !="":
    app.run(host=host,port=port,debug=True)
else:
    print("host or port not spacified")