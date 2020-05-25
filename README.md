 
# alta3 github-automation

This repo is a step-by-step guide/script for managing organization wide github issue labels across all projects.

Result:  
![Github labels](https://static.alta3.com/blog/github-labels.png)

## Prerequisites

- Create a github [Personal access token](https://github.com/settings/tokens)
  - Give it a name
  - **Only** select the `repo` scope
- User has access to the github organization 

## Install

```
python3.8 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel
python -m pip install -r requirements.txt
```

**Example `.env` file**:

```
GITHUB_USER_TOKEN="<YOUR_TOKEN_HERE>"
LABELS_TOKEN=${GITHUB_USER_TOKEN}
LABELS_USERNAME="<YOUR_USERNAME>"

```

### Run

**List all alta3 repos**:

```
python list-all-repos.py
```

**Make a backup of all current labels**

```
mkdir -p repo-labels
python list-all-repos.py | xargs -I {} labels fetch --owner alta3 --repo {} --filename repo-labels/{}-labels.toml
```

**Setup a common set of labels for every repo**

View/edit `default-labels.toml` for the list of labels.

```
python list-all-repos.py | xargs -I {} labels sync --owner alta3 --repo {} --filename default-labels.toml
```
