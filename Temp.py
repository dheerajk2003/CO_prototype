from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def initClient():
    client = genai.Client(api_key=os.getenv("GEMINIAPIKEY"))
    print("[Info] Successfully created Gemini Client")
    return client


def GetTest(client, body):
    res = client.models.generate_content(model="gemini-2.5-pro-exp-03-25", contents=str(body))

    return res.text



