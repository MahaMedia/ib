from flask import Flask, render_template, send_from_directory, jsonify
from test import test
import os
import subprocess
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.template')
    
@app.route('/test', methods=['GET'])
def show_test_script():
    try:
        result = subprocess.run(
            ["/var/www/mahamedia.us/intelligencebank_tools/venv/bin/python3",
             "/var/www/mahamedia.us/intelligencebank_tools/test.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"message": "Test executed successfully", "output": result.stdout.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
