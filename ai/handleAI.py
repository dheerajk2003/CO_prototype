from ai.GetTest import Gemini, Llama, GPT, DeepSeek
import time

class handleAI:
    def __init__(self):
        self.geminiClient = Gemini()
        self.llamaClient = Llama()
        self.gptClient = GPT()
        self.deepseekClient = DeepSeek()    

    def GenerateResponses(self, prompt):
        start = time.time()
        wtr = open("data/data_gemini.md", 'w')
        wtr.write(self.geminiClient.GetTest(prompt))
        wtr.close()
        print(f"Successfully Generated Gemini 2.5 Response ({time.time() - start} sec)")

        start = time.time()
        wtr = open("data/data_llama.md", 'w')
        wtr.write(self.llamaClient.GetTest(prompt))
        wtr.close()
        print(f"Successfully Generated Llama 4 Response ({time.time() - start} sec)")


        start = time.time()
        (think, test) = self.deepseekClient.GetTest(prompt)
        wtr = open("data/data_deekseek.md", 'w')
        wtr.write(test)
        wtr.close()
        
        wtr = open("data/thinking_deepseek.txt", 'w')
        wtr.write(think)
        wtr.close()
        print(f"Successfully Generated Deepseek R1 Response  ({time.time() - start} sec)")
