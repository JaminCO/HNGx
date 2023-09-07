from flask import Flask, jsonify, request
import datetime
from datetime import timezone

app=Flask(__name__)
@app.route('/api',methods=['GET',])
def home():
    args = request.args
    slack_name = args.get("slack_name")
    track = args.get("track")
    current_day = datetime.date.today().strftime("%A")
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": datetime.datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": "https://github.com/JaminCO/HNGx/blob/main/filen_name.ext",
        "github_repo_url": "https://github.com/JaminCO/HNGx",
        "status_code": 200
    }
    return jsonify(response)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)