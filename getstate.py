from flask import Flask, jsonify, request
from dotenv import load_dotenv
import requests, os

load_dotenv()
IPINFO_APIKEY = os.getenv("IPINFO_APIKEY") # https://ipinfo.io/products/ip-geolocation-api

app = Flask(__name__)

@app.route("/getstate", methods=["GET"])
def get_state():
    try:
        user_ip = request.remote_addr
        url = f"https://ipinfo.io/{user_ip}?token={IPINFO_APIKEY}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            response_data = response.json()
            return jsonify({
                "state": response_data.get("region"),
                "country": response_data.get("country") # want to verify that this is US
            })
        else:
            return jsonify({"Error": response.text}), 500

    except requests.exceptions.RequestException:
        return jsonify({"Error": "There was an issue fetching the state information."}), 500

    except Exception:
        return jsonify({"Error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)
