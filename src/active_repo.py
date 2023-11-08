import os
import subprocess
import json
from github import Github as gh, Auth
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(raise_error_if_not_found=True))

# Function to get the URL of the remote repository
def get_remote_url():
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.dom.url"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print(result)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(e)

# Function to get the latest commit date
def get_latest_commit_date():
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

# Function to check if the repository is active
# For this example, "active" is arbitrarily defined as having a commit in the last 90 days
def is_repo_active():
    from datetime import datetime, timedelta
    latest_commit_date = get_latest_commit_date()
    if latest_commit_date:
        last_commit_datetime = datetime.strptime(latest_commit_date, '%a %b %d %H:%M:%S %Y %z')
        return (datetime.now(last_commit_datetime.tzinfo) - last_commit_datetime) < timedelta(days=90)
    else:
        return False

# Use the functions
def repo_main():
    gh_token = os.getenv('GITHUB_TOKEN')
    auth = Auth.Token(gh_token)
    g = gh(auth=auth).get_user()
    repos_ls = []
    repo = 'depend-en-moi' # list the repos and make a selection
    for repos in g.get_repos():
        repos_ls.append(repos.name)
        # to see all the available attributes and methods
    #remote_url = get_remote_url()
    print(repos_ls)
    try:      
        get_repo = g.get_repo(repo)
        #get_repo.edit(has_wiki=False)
        print(f"Retrieved{get_repo}")
    except Exception as e:
        print("Error is: {}", e)

    return print("Success")
            
       
