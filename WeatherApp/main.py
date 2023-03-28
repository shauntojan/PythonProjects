import requests
import json
import os
city = input("Enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key= c204ea3b0ead43ecb4f175254232703&q={city}"

r = requests.get(url)
# print(r.text)

wdic= json.loads(r.text)
w=(wdic["current"]["temp_c"])


command = f"  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The weather in {city} is {w} degree celsius');\""
textToSpeak = f"{command}  "
os.system(command)
