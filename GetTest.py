# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
# -H 'Content-Type: application/json' \
# -X POST \
# -d '{
#   "contents": [{
#     "parts":[{"text": "Explain how AI works"}]
#     }]
#    }'


import requests
import json
import os


# print(os.environ)

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key="
headers = {
    'Content-Type': 'application/json'
}
content = {
    "contents": [{
        "parts": [{"text": "Explain AI in 20 words"}]
    }]
}

def GetTest(body):
    api=""
    with open(".env", 'r') as f:
        api = f.read()

    x = requests.post((url+api), headers=headers, data=json.dumps(body))
    data = x.json();
    return data["candidates"][0]["content"]["parts"][0]["text"]
