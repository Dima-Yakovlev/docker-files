from flask import Flask
import subprocess
import psutil
import os
app = Flask(__name__)

base_html = '<ul> <li><a href="/start_import_script">Start ImortScript</a> </li> <li><a href="/get_list_processes"> Show List Process</a></li></ul>'

@app.route('/')
def home():
    return base_html

@app.route('/start_import_script')
def start_import_script():
    p = subprocess.Popen("ps -aux | grep python", stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    os.system("python3 -u /app/nt_import/nt_importd.py /app/nt_import/logs/run/nt_importd.pid /app/nt_import/logs/nt_importd.log restart")
    return f'{base_html}<br><h1>Script Restart</h1> <br>{out}<br>{err}'
    
@app.route('/get_list_processes')
def get_list_processes():
    arr_list = []
    arr_list.append("<ul>")
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            arr_list.append(f"<li>{processName}:::{processID}</li>")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        arr_list.append("</ul>")
        li = " ".join(arr_list)
        return f"{base_html}<br>{li}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")