from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/subdomain", methods=["GET"])
def subdomain():
    user_input = request.args.get("user_input")
    if not user_input:
        return "Error: Input not provided"
    
    processed_result = subprocess.check_output(['python3', 'subdomain_scanner.py', user_input])
    processed_result = processed_result.decode('utf-8')
    return processed_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4017)
