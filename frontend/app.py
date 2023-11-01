from flask import Flask, render_template, request, redirect, url_for
import requests
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')

@app.route('/vulner', methods=['GET'])
def vulner():
    return render_template('vulner.html')

@app.route('/output', methods=['GET'])
def output():
    return render_template('output.html')

@app.route('/vulneroutput', methods=['GET'])
def vulneroutput():
    return render_template('vulneroutput.html')

@app.route("/iplocate", methods=["GET", "POST"])
def iplocate():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://iplocator:4011/iplocate?user_input={user_input}")
        processed_result = response.text

        if "Opening Location in browser" in processed_result:
            map_link = processed_result.split("Opening Location in browser: ")[1]
            return render_template('output.html', result=processed_result, map_link=map_link)
        return render_template('output.html', result=processed_result)
    return render_template('info.html')

@app.route("/phone_scan", methods=["GET", "POST"])
def phone_scan():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://phone_scan:4012/phone_scan?user_input={user_input}")
        processed_result = response.text

        return render_template('output.html', phone_scan_result=processed_result)
    return render_template('info.html')

@app.route("/pdfanalysis", methods=["GET", "POST"])
def pdfanalysis():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            pdf_path = '/app/pdf_files/temp.pdf'
            pdf_file.save(pdf_path)

            try:
                response = requests.get(f"http://pdfanalysis:4013/pdfanalysis?user_input={pdf_path}")
                processed_result = response.text
                return render_template('output.html', pdfanalysis_result=processed_result)
            except subprocess.CalledProcessError as e:
                    error_message = f"An error occurred: {e.output.decode('utf-8')}"
                    return render_template('output.html', pdfanalysis_result=error_message)
        else:
            return redirect(url_for('info'))
        
@app.route("/email_scrape", methods=["GET", "POST"])
def email_scrape():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://email_scrape:4014/email_scrape?user_input={user_input}")
        processed_result = response.text

        return render_template('output.html', email_scan_result=processed_result)
    return render_template('info.html')

@app.route("/links_scrape", methods=["GET", "POST"])
def links_scrape():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://links_scrape:4015/links_scrape?user_input={user_input}")
        processed_result = response.text

        return render_template('output.html', link_scan_result=processed_result)
    return render_template('info.html')

@app.route("/number_info", methods=["GET", "POST"])
def number_info():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://number_inform:4016/number_info?user_input={user_input}")
        processed_result = response.text

        return render_template('output.html', number_info_result=processed_result)
    return render_template('info.html')

@app.route("/subdomain", methods=["GET", "POST"])
def subdomain():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://subdomain_scan:4017/subdomain?user_input={user_input}")
        processed_result = response.text

        return render_template('output.html', subdomain_result=processed_result)
    return render_template('info.html')

@app.route("/clickjack", methods=["GET", "POST"])
def clickjack():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = requests.get(f"http://clickjacking:4018/clickjack?user_input={user_input}")
        processed_result = response.text

        return render_template('vulneroutput.html', clickjack_result=processed_result)
    return render_template('vulner.html')

@app.route("/sql", methods=["GET", "POST"])
def sql():
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            response = requests.get(f"http://sql_injection:4019/sql?user_input={user_input}")
            processed_result = response.text

            return render_template('vulneroutput.html', sql_result=processed_result)
        return render_template('vulner.html')
    except ConnectionAbortedError as exception:
        print(exception.message)

@app.route("/nmap_scan", methods=["GET", "POST"])
def nmap_scan():
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            response = requests.get(f"http://nmap_scan:4020/nmap_scan?user_input={user_input}")
            processed_result = response.text

            return render_template('vulneroutput.html', nmap_scan_result=processed_result)
        return render_template('vulner.html')
    except ConnectionAbortedError as exception:
        print(exception.message)

@app.route("/xss", methods=["GET", "POST"])
def xss():
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            response = requests.get(f"http://xss_scan:4021/xss?user_input={user_input}")
            processed_result = response.text

            return render_template('vulneroutput.html', xss_result=processed_result)
        return render_template('vulner.html')
    except ConnectionAbortedError as exception:
        print(exception.message)

@app.route("/hostheader", methods=["GET", "POST"])
def hostheader():
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            response = requests.get(f"http://hostheader:4022/hostheader?user_input={user_input}")
            processed_result = response.text

            return render_template('vulneroutput.html', hostheader_result=processed_result)
        return render_template('vulner.html')
    except ConnectionAbortedError as exception:
        print(exception.message)

@app.route("/ipdomain", methods=["GET", "POST"])
def ipdomain():
    try:
        if request.method == "POST":
            user_input = request.form.get("user_input")
            response = requests.get(f"http://ipdomain:4023/ipdomain?user_input={user_input}")
            processed_result = response.text

            return render_template('vulneroutput.html', ipdomain_result=processed_result)
        return render_template('vulner.html')
    except ConnectionAbortedError as exception:
        print(exception.message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
