import os

def InstallPipPackage(PackageList): # func install package
    for PackageName in PackageList:
        os.system("pip install " + PackageName)

InstallPipPackage(['colorama', 'requests', 'pyinstaller', 'neofetch-win']) # install requests, colorama

