import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_location():
    ip = request.args.get('ip')
    timezone = requests.get(f'https://api.ipgeolocation.io/timezone?apiKey=36756032b8c14b2eaf59155f8278afa9&ip={ip}').json()
    timezone = timezone['timezone']
    return timezone


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
