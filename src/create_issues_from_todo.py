import os
from github import Github as gh
from github import Auth
from active_repo import get_remote_url, repo_main
from dotenv import load_dotenv
load_dotenv()

import json

todo_filename = 'TODO.txt'
json_filename = './data/data.json'

# Function to add an entry to a JSON file
def add_entry_to_json(title=None, body=None, filename='./data/data.json'):
    try:
        # Load existing data from the file
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, start a new list
        data = []
    
    # Add new entry to data with incremented item number
    curr_idx = len(data) + 1
    new_entry = {
        "item": curr_idx,
        "title": title,
        "body": body
    }
    data.append(new_entry)
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to retrieve and delete an entry by its title
def retrieve_and_delete_entry_by_title(title, todo_file, json_file):
    try:
        # Load the JSON file into memory
        with open(todo_file, 'r') as file:
            data = file.readlines()
        data = [entry for entry in data if not title(entry)]
    
        # Write the modified data back to the file
        with open(json_file, 'w', encoding=) as file:
            json.dump(data, json_file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing data found for {}", title)
        

    # Find the entry by title
    entry = next((entry for entry in data if entry['title'] == title), None)
    
    # If the entry was found, delete it
    if entry:
        data.remove(entry)
        print(f"Entry with title '{title}' has been retrieved and deleted.")
    else:
        print(f"No entry with title '{title}' found.")
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    return entry

# Parse 'TODO.md' and extract todo items
def parse_todo_file(filename):
    with open(filename, 'r') as file:
        todos = file.readlines()
    return [line.strip() for line in todos if line.strip()]

# Check if an issue already exists
def issue_exists(repo, title):
    issues = repo.get_issues(state='open')
    return any(issue.title == title for issue in issues)

# Create an issue if it doesn't exist
def create_issue_main(repo, title):
    
    #set to false for now
    debug = True
    
    repo = repo_main()
    todos = parse_todo_file('../TODO.md')
    
    for td in todos:
        if issue_exists(repo=repo, title=td):
            print("issue exists")
        else:
            try:
                repo.create_issue(title=td, body=input(f"Additional info for {title}?"))
                if debug:
                    print("create issue complete")
                    break
                
                    
                
            except Exception as e:
                print(e)
                continue
                
    print(f"{len(todos)} issues to {repo.name}")
        
if __name__ == "__main__": 
    main()
    
    
    
        
    
    r
    

        
main_function()

