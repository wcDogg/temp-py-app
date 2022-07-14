# MyApp

A project template for Python command line apps.


## Do Something

```
py app.py
```

## VS Code venv

```
py -3 -m venv venv
venv/Scripts/activate.bat
# Select Interpreter. Kill / new bash terminal
which pip3
py -m pip install -r requirements.txt --upgrade
```

## .env

`.env` is for storing sensitive data, like API credentials. NEVER upload this file to the Internet. 

* Change `.env.example` to `.env`.
* Ensure `.env` is present in `.gitignore`.
* Update / add sensitive info in `.env`. 
* See `configure.py` for example use of `.env`. 


## configure.py

`configure.py` stores the app's constants / globals. Use this file to adjust defaults to match your workflow. 


## Documentation

Most documentation is in the files themselves. Topics that require more explanation are located in the [App Documentation](/docs/README.md).

