import os
import sys
from dotenv import load_dotenv
from github import Github

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("GITHUB_USER_TOKEN")
    
    g = Github(token)
    alta3 = g.get_organization('alta3')
    
    for repo in alta3.get_repos():
        print(repo.name)

    if token == None:
       sys.stderr.write("\nGITHUB_USER_TOKEN not provided, only public repos listed!\n")
