import os
from subprocess import call, DEVNULL
import platform

class Startup:
    osName = None

    def __init__(self):
        self.osName = platform.system()

    def GetVenvCreateCommand(self):
        venvCommand = ""
        if self.osName == 'Linux':
            venvCommand = "pip install virtualenv && virtualenv venv && "
            venvCommand += "source /venv/bin/activate && "
            venvCommand += "pip3 install numpy tensorflow gym keras keras-rl2 Pillow torch torchvision torchaudio xformers && "
            venvCommand += "deactivate"
        elif self.osName == 'Windows':
            venvCommand = "py -m venv venv && "
            venvCommand += ".\\venv\\Scripts\\activate.bat && "
            venvCommand += ".\\venv\\Scripts\\pip.exe install numpy tensorflow gym keras keras-rl2 Pillow xformers && "
            venvCommand += ".\\venv\\Scripts\\pip.exe install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117"
            venvCommand += ".\\venv\\Scripts\\deactivate.bat"
        
        return venvCommand
    
    def CreateVenv(self):
        if os.path.exists("venv") == True:
            return

        print("Preparing virtual environment ...")
        result = call(self.GetVenvCreateCommand(), shell=True)
        _ = print("Virtual environment is created") if result == 0 else print("Error")
    
    def GetStartCommand(self):
        guiCommand = ""
        if self.osName == 'Linux':
            guiCommand = "source /venv/bin/activate && python3 main.py"
        elif self.osName == 'Windows':
            guiCommand = ".\\venv\\Scripts\\activate.bat && .\\venv\\Scripts\\python.exe main.py"
        
        return guiCommand
    
    def Start(self):
        print("Starting ...")
        guiCommand = self.GetStartCommand()
        result = call(guiCommand, shell=True)
        
        if self.osName == 'Linux':
            result = call("deactivate", shell=True, stdout=DEVNULL)
        elif self.osName == 'Windows':
            result = call(".\\venv\\Scripts\\deactivate.bat", shell=True, stdout=DEVNULL)
        
        if result == 0:
            print("Finished successfully")


if __name__ == "__main__":
    startup = Startup()
    startup.CreateVenv()
    startup.Start()