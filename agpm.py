import json
import os
import requests
import sys
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

def lookup(item):
    response = requests.get("https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/metadata.json")
    response.raise_for_status()
    metadata = json.loads(response.text)
    clouddesc = metadata.get('description')
    cloudnotes= metadata.get('releaseNotes')
    print("package name: " + str(item))
    print("description: " + str(clouddesc))
    print("latest release notes: " + str(cloudnotes))

def install(item):
    os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/install.sh && bash install.sh && rm install.sh")

def uninstall(item):
    os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/uninstall.sh && bash uninstall.sh && rm uninstall.sh")

def update(item):
    response = requests.get("https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/metadata.json")
    response.raise_for_status()
    metadata = json.loads(response.text)
    cloudver = metadata.get('version')
    file_path = os.path.join(os.path.expanduser('~'), '.agpm', item, 'metadata.json')
    with open(file_path, 'r') as f:
        localmetadata = json.load(f)
    localver = localmetadata.get('version')
    if localver != cloudver:
        os.system("curl -O https://eyescary-development.github.io/CDN/agpm_packages/"+item+"/protocols/update.sh && bash update.sh && rm update.sh")
    else:
        print("Package already up to date, command already satisfied")

def operate(task, app):
    if checkpackagelist(app):
        match task:
            case "install":
                install(app)
            case "uninstall":
                uninstall(app)
            case "update":
                update(app)
            case "search":
                lookup(app)
    else:
        print("package doesn't exist :(")

def main():
    if len(sys.argv) != 3:
        print("Usage: agpm-pyp <task> <app>")
        sys.exit(1)

    _, task, app = sys.argv
    operate(task, app)

if __name__ == "__main__":
    main()

