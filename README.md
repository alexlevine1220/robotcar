# User
pip3 install robotcar

# Developer

## Edit
### 1. pip3 install -e git+https://github.com/SeanHwangG/robotcar#egg=robotcar
- allows to import robotcar without having it at the same folder
### 2. git branch -b <branch_name>
### 3. git push --set-upstream origin <branch_name>
### 4. Make a pull request at https://github.com/SeanHwangG/robotcar

## Publish
### 1. Change version in setup.py
- Be consistent with branch
### 2. python3 setup.py sdist 

- It updates contents in /dist directory=

### 3. twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

- You need id and password in order to run the following command
