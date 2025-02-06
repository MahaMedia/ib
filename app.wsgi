import sys
import os

venv_path = "/var/www/mahamedia.us/ib/venv"
sys.path.insert(0, os.path.join(venv_path, "lib/python3.12/site-packages"))
sys.path.insert(0, "/var/www/mahamedia.us/ib")

from app import app as application
