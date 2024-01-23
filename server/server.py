import os
from pathlib import Path
from flask_cors import CORS  # Import CORS from Flask-CORS
from flask import Flask, jsonify, request, send_from_directory
import csv


app = Flask(__name__)
CORS(app)

# historyData = [
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 6},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 1},
#             {"x": 20, "y": 9},
#         ],
#     },
#     {
#         "id": "Metric History",
#         "data": [
#             {"x": -20, "y": 1},
#             {"x": -10, "y": 7},
#             {"x": 0, "y": 2},
#             {"x": 10, "y": 6},
#             {"x": 20, "y": 5},
#         ],
#     },
# ]
# speedData = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
# boomData = speedData[::-1]
# gpaData = [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]


# Define the absolute path to the 'client/build' directory
buildFilePath = Path(__file__).resolve().parent.parent / 'client' / 'build'
print(buildFilePath, ": path")

csvFilePath = Path(__file__).resolve().parent / 'utils' / 'data_csv.csv'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print("hi")
    if not path or path == 'index.html':
        # Serve 'index.html' for the root path or explicit requests for it
        return send_from_directory(buildFilePath, 'index.html')
    else:
        # Serve other files from the 'fe/build' directory
        return send_from_directory(buildFilePath, path)


@app.route('/history-data', methods=['GET'])
def hello():
    time = int(request.args.get('time'))
    if time >= 260:
        time = 0

    # Read CSV data
    with open(csvFilePath, newline='') as csvFile:
        reader = csv.DictReader(csvFile)
        history_data = []

        for _ in range(time + 1):
            row = next(reader, None)

        if row:
            # Initialize data list if it doesn't exist
            if 'historyData' not in row:
                row['historyData'] = []

            # Append the current data point
            row['historyData'].append({
                "id": "Metric History",
                "data": [
                    {
                        "x": float(row["time"]),
                        "y": float(row["metric"])
                    },
                ]
            })

            gpaData = int(row["gpa"])
            boomData = int(row["boom"])
            speedData = int(row["speed"])

            # Return historyData as an array
            return jsonify({'historyData': row['historyData'], "gpaData": gpaData, "boomData": boomData, "speedData": speedData}), 200

        else:
            return jsonify({'error': 'Invalid params'})




if __name__ == '__main__':
    app.run(debug=True)
