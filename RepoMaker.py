import requests, os, json

print("[ GITHUB REPOSITORY MAKER ]\n")
name = input("Repo name --> ")
state = int(input("Private or Public ? 0 or 1 --> "))
description = input("Describe your repo, empty if not --> ")

TOKEN = os.environ['GITHUB_TOKEN']
URL = "https://api.github.com/user/repos"

HEADERS = {
    "Accept": "application/vnd.github+json",
    'Authorization': f"Bearer {TOKEN}",
    'X-Github-Api-Version': "2022-11-28"

}

DATA = {
    "name": name,
    "private": False if state else True,
    "description": description,    
    
}

req = requests.post(URL, headers=HEADERS, json=DATA)

if req.status_code == 201: # CREATED
    data = req.json()
    repo_url = data['html_url'] + ".git"
    os.system(f"echo {repo_url} | clip")
    print(f"You repository with the url {repo_url} has been created and have been copy to your clipboard !")
    
else:
    print(req, req.text) # print error