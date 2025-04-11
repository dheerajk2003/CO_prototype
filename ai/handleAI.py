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
        wtr = open("data/data_gemini.json", 'w')
        wtr.write(self.geminiClient.GetTest(prompt))
        wtr.close()
        print(f"Successfully Generated Gemini 2.5 Response ({time.time() - start} sec)")

        start = time.time()
        wtr = open("data/data_llama.json", 'w')
        wtr.write(self.llamaClient.GetTest(prompt))
        wtr.close()
        print(f"Successfully Generated Llama 4 Response ({time.time() - start} sec)")


        start = time.time()
        (think, test) = self.deepseekClient.GetTest(prompt)
        wtr = open("data/data_deekseek.json", 'w')
        wtr.write(test)
        wtr.close()
        
        wtr = open("data/thinking_deepseek.txt", 'w')
        wtr.write(think)
        wtr.close()
        print(f"Successfully Generated Deepseek R1 Response  ({time.time() - start} sec)")

    def ChooseResponse(self, prompt):

        aiModels = ["deekseek", "gemini", "llama"]
        resInstruction = []
        while(True):
            try:
                resIns = (prompt, "" , "")
                choice = int(input("Choose One of the AI Response:"))
                resIns[1] = open("data/data_"+aiModels[choice-1]+".json").read()
                resIns[2] = input("Any further instructions to improve the Response (Ctrt+Z + Return):\n")

                
                resInstruction.append(resIns)
            except EOFError:
                print("Ok. Saving the Instructions provided till this point.")
                break
        
