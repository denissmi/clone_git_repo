# Clone Git Repo
Clones or pulls git repo

##### Setting up environment:
1. Install python
2. Install virtualenv: `pip install virtualenv`
3. Create virtual environment: `virtualenv <any_path>/venv`
4. Activate the virtual environment: `<any_path>/venv/Scripts/activate`
5. Install required modules: `pip install -r <local_repo_path>/requirements.txt`

##### Example of the usage:
`python clone_git_repo.py --git-url https://github.com/denissmi/clone_git_repo --branch master
--local_path C:\clone_git_repo`
