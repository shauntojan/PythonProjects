import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0. Created by SHAUN TOJAN")
    while (True):
        str = input("Enter text to speak : ");
        if (str == "bye"):
            break
        command = f"  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{str}');\""
        textToSpeak = f"{command}  "
        os.system(command)