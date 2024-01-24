# flask imports
from flask_cors import CORS  
from flask import Flask, jsonify, request, send_from_directory

# library imports
import os
from pathlib import Path
import csv
from collections import deque


app = Flask(__name__)
CORS(app)



# Define the absolute path to the 'client/build' directory
buildFilePath = Path(__file__).resolve().parent.parent / 'client' / 'build'

csvFilePath = Path(__file__).resolve().parent / 'utils' / 'data_csv.csv'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if not path or path == 'index.html':
        # Serve 'index.html' for the root path or explicit requests for it
        return send_from_directory(buildFilePath, 'index.html')
    else:
        # Serve other files from the 'fe/build' directory
        return send_from_directory(buildFilePath, path)


historyData = [
    {
        "id": "Metric History",
        "data": [
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
            {"x": 0, "y": 0},
        ],
    }
]

# Initialize the deque with the initial data
historyDeque = deque(historyData[0]["data"], maxlen=5)

@app.route('/history-data', methods=['GET'])
def displayHistoryData():
    global historyDeque

    time = int(request.args.get('time'))
    if time >= 521:
        time = 0
    
    # Read CSV data
    with open(csvFilePath, newline='') as csvFile:
        reader = csv.DictReader(csvFile)

        for _ in range(time + 1):
            row = next(reader, None)

        if row:
            gpaData = int(row["gpa"])
            boomData = int(row["boom"])
            speedData = int(row["speed"])

            # Append the current data point to the deque
            historyDeque.append(
                {
                    "x": float(row["time"]),
                    "y": float(row["metric"])
                })

            # Convert deque to list before serializing to JSON
            history_data = list(historyDeque)

            # Return historyData as an array
            return jsonify({'historyData': [{'id': 'Metric History', 'data': history_data}], "gpaData": gpaData, "boomData": boomData, "speedData": speedData}), 200

        else:
            return jsonify({'end': True}), 200



if __name__ == '__main__':
    app.run(debug=True)
