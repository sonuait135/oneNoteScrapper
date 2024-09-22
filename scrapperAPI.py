
# Create a Crew to execute the task
from fastapi.encoders import jsonable_encoder


from crewai import Crew, Process

import time
import threading
from flask import Flask, jsonify, request
from functools import wraps
from Task import invoke_Crew
import json
from flask_cors import CORS

from EmailHelper import send_email

def timeout_decorator(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start a timer to simulate timeout
            timer = threading.Timer(seconds, lambda: print("Request timed out!"))
            timer.start()

            try:
                # Execute the original function
                return func(*args, **kwargs)
            finally:
                # Cancel the timer if the request finishes before timeout
                timer.cancel()
        return wrapper
    return decorator

app = Flask(__name__)
CORS(app)

globalData=None
@app.route('/process-response', methods=['POST'])
# @timeout_decorator(1200)  # Set timeout to 120 seconds
def process_response():

    try:
        global globalData
        if (globalData == None):
            data = request.get_json()
            crew_output=invoke_Crew(data)
            # globalData = crew_output
        print("Scraping Done")
        if data.get('isReddit') == True:
            send_email( 'Reddit: Customer Feedback Summary', crew_output)

        if data.get('isGooglePlayStore') == True:
            send_email( 'Google Play: Customer Feedback Summary', crew_output)

        # # Print the output
        # print(crew_output)

        return jsonable_encoder(crew_output), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
