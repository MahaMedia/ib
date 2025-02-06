import sys
import os

# os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/var/www/mahamedia.us/intelligencebank_tools/venv/browser_binaries"

venv_path = "/var/www/mahamedia.us/ib/venv"
sys.path.insert(0, os.path.join(venv_path, "lib/python3.12/site-packages"))
sys.path.insert(0, "/var/www/mahamedia.us/ib")

from app import app as application
