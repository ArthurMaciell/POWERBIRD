import schedule
import time as tm
from datetime import time
from schedule import repeat, every
import subprocess

def listar():
    subprocess.run([
        "C:\\Users\\Orçamento\\OneDrive - GRUPO RETEC\\02. Engenharia\\Dep. Orçamentos\\POWERBI\\AUTOMACAO RD\\autord\\Scripts\\python.exe",
        "C:\\Users\\Orçamento\\OneDrive - GRUPO RETEC\\02. Engenharia\\Dep. Orçamentos\\POWERBI\\AUTOMACAO RD\\scripts\\listar.py"
    ], check=True)

schedule.every().day.at("1:04").until().do(listar)
#schedule.every().hour.at(":56").do(listar)

while True:
    schedule.run_pending()
    tm.sleep(1)
    