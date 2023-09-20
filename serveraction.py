from flask import Flask,jsonify,request
import subprocess

app = Flask(__name__)


def GetDevices():
        while True:
            devices = subprocess.check_output("adb devices")
            p = str(devices).replace("b'List of devices attached","").replace('\\r\\n',"").replace(" ","").replace("'","").replace('b*daemonnotrunning.startingitnowonport5037**daemonstartedsuccessfully*Listofdevicesattached',"")
            if len(p) > 0:
                listDevices = p.split("\\tdevice")
                listDevices.pop()
                return listDevices


@app.route('/', methods=['GET', 'POST'])

def hello_world():
    data = request.json
    datarun = data['action']

    if datarun == 'getdevices' :
        devideslise = GetDevices()
        print(devideslise)
        return jsonify(devideslise)
    if datarun == 'ckicj' :
        subprocess.call(f"adb -s emulator-5554 shell input tap 206 178", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=2020)