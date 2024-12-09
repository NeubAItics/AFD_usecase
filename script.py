import os
from git import Repo

def remove_file_from_history(repo_path, file_to_remove):
    repo = Repo(repo_path)
    
    # Ensure repository is clean
    if repo.is_dirty():
        raise Exception("Repository has uncommitted changes. Commit or stash them before proceeding.")
    
    # Remove file from repository
    if file_to_remove in repo.git.ls_files():
        print(f"Removing {file_to_remove} from tracking...")
        repo.git.rm("--cached", file_to_remove)
    
    # Add .env to .gitignore
    gitignore_path = os.path.join(repo_path, ".gitignore")
    with open(gitignore_path, "a") as gitignore:
        gitignore.write(f"\n{file_to_remove}\n")
    
    repo.index.add([gitignore_path])
    repo.index.commit(f"Remove {file_to_remove} from history and add to .gitignore")
    
    # Rewrite history to remove the file
    print("Rewriting history to remove sensitive file...")
    repo.git.filter_branch("--tree-filter", f"rm -f {file_to_remove}", "--", "--all")
    
    # Garbage collect to finalize removal
    repo.git.gc("--prune=now", "--aggressive")
    print("File successfully removed from history!")

# Path to your repository and file to remove
repo_path = r"D:\NB\PM_Karthick\Analyze Financial Docs with GPT Vision"
file_to_remove = ".env"

try:
    remove_file_from_history(repo_path, file_to_remove)
    print("Process completed. Push your changes with '--force' to update the remote.")
except Exception as e:
    print(f"Error: {e}")