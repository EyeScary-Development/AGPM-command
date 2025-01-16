import os
import requests
#temp list of packages
pkglist=[]

url = 'https://eyescary-development.github.io/CDN/agpm_packages/packagelist.txt'
def checkpackagelist(item):
    response = requests.get(url)
    response.raise_for_status()
    pkglist = response.text.splitlines()
    if item in pkglist:
        return True
    else:
        return False

def install(item):
    os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/install.sh && bash install.sh && rm install.sh")

def uninstall(item):
    os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/uninstall.sh && bash uninstall.sh && rm uninstall.sh")

def update(item):
    os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/update.sh && bash update.sh && rm update.sh")

def operate():
    task, app=input("AGPM mode (Just ctrl C to quit): "), input("Program to operate on: ")
    if checkpackagelist(app):
        match task:
            case "install":
                install(app)
            case "uninstall":
                uninstall(app)
            case "update":
                update(app)

def main():
    while True:
        operate()
main()
