from flask import Flask, render_template
from zoomus import ZoomClient
import requests
import json
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

API_KEY = 'y39UHybfTHmUbGPFotQ8cg'
API_SECRET = 'n1VrlxhAU6kXveBYpQHJMWosYhHmEMOnR36Q'

zoom_client = ZoomClient(api_key=API_KEY, api_secret=API_SECRET)
user_id="rsmejia@oj.gob.gt"

@app.route('/')
def index():

    response = zoom_client.meeting.list(user_id=user_id, type='upcoming')
    meetings_list = []
    
    if response.status_code == 200:
        try:
            meetings_list = response.json().get('meetings', [])
        except ValueError as e:
            print('Error al decodificar la respuesta JSON: ', e)
    else:
        print('La llamada a la API de Zoom falló con el código de estado HTTP: ', response.status_code)
            
    return render_template('index.html', meetings=meetings_list, user=user_id)

@app.route('/dark_mode')
def dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
