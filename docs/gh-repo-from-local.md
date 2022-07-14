# GitHub Repo from Local Directory

See: [Adding an existing project to GitHub using the command line](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line)

```
# Copy a local folder (template)
Copy-Item -Path "D:\github\.project" -Destination "D:\github\pngsqu" -recurse -Force

# cd to the new directory and view contents
cd D:\github\test
Get-ChildItem

# Create the repo
git init -b main
git add . && git commit -m "initial commit"
gh repo create

# Follow these prompts
Initialized empty Git repository in D:/GitHub/test/.git/

? What would you like to do? Push an existing local repository to GitHub
? Path to local repository (.)

? Path to local repository .
? Repository name (test)

? Repository name test
? Description A short description

? Description A short description
? Visibility Public
✓ Created repository wcDogg/test on GitHub
? Add a remote? Yes
? What should the new remote be called? (origin)

? What should the new remote be called? origin
✓ Added remote git@github.com:wcDogg/test.git
? Would you like to push commits from the current branch to "origin"? Yes
✓ Pushed commits to git@github.com:wcDogg/test.git
```