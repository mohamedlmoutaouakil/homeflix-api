# Homeflix API
This is a simple flask app, it manages your media gallery (a movies folder for example) by creating a database of the media present in your gallery. The app allows you to access your media gallery database by a REST API operations.

## Setting up the environment
The project is developped in a pipenv virtual environment, which contains the dependencies necessary for thr project to run. Therefore, if not already installed, you have to install pipenv:
```
python -m pip install pipenv
```
or
```
py -m pip install pipenv
```
Then start the virtual environment:
```
pipenv shell
```
## Starting the server
Before starting the homeflix-api server, you have to start the streaming server: https://github.com/mohamedlmoutaouakil/homeflix-streaming-server

Now you can start the server. To do so, run the following command:
```
python wsgi.py
```
and then it will ask to provide the absolute path to your media directory.

Once the server is running you check the swagger documentation to see the REST operations provided by this application in: http://localhost:5000/ui

Now go ahead and start the homeflix React app : https://github.com/mohamedlmoutaouakil/homeflix