from google import genai
from groq import Groq
from openai import OpenAI
from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
import os
load_dotenv()

class Gemini:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
        print("[Info] Successfully created Google (Gemini) Client")

    def createChat(self):
        return self.client.chats.create(model="gemini-2.5-pro-exp-03-25")

    def GetTest(self,body):
        res = self.client.models.generate_content(model="gemini-2.5-pro-exp-03-25", contents=str(body))
        return res.text.split("```json", 1)[1].rsplit("```", 1)[0]
      
class Llama:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_KEY"))
        print("[Info] Successfully created Groq (Llama) Client")

    def GetTest(self, body):
        res = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": str(body),
                    }
                ],
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                )
        return res.choices[0].message.content.split("```json", 1)[1].rsplit("```", 1)[0]
    
class GPT:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
        print("[Info] Successfully created OpenAI (GPT) client")
    
    def GetTest(self, body):
        res = self.client.responses.create(
            model="o3-mini",
            input=str(body)
        )

        return res.output[0].content[0].text.split("```json", 1)[1].rsplit("```", 1)[0]

class DeepSeek:
    def __init__(self):
        self.client = KrutrimCloud(api_key=os.getenv("KRUTRIM_KEY"))
        print("[Info] Successfully create Krutrim (Deepseek) client")

    def GetTest(self, body):
        res = self.client.chat.completions.create(model="DeepSeek-R1", messages=[
            {"role" : "user", "content": str(body)}
        ])
        res = res.choices[0].message.content.rsplit("</think>")
        
        testContent = res[-1].split("```json", 1)[1].rsplit("```", 1)[0]
        thinkingData = '\n'.join(res[0:-1]).removeprefix("<think>")
        return (thinkingData, testContent)