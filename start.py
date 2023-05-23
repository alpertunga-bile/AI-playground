from VenvManager import VenvManager

if __name__ == "__main__":
    venvManager = VenvManager("venv")

    if venvManager.IsEnvironmentCreated is False:
        venvManager.CreateEnvironmentWPackageNames(packagesPath="packages.txt")
        venvManager.RunCommandInEnvironment(".\\venv\\Scripts\\pip.exe install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
        venvManager.RunCommandInEnvironment(".\\venv\\Scripts\\pip.exe install xformers")

    venvManager.RunFile("main.py")