Discovering Time -Zone using IP app


Introduction
------------

This project is part of my entrance exam for SAVVY company.
This project is an application that allows Time-zone checking by IP Address.

* Third-party resolver
  https://ipgeolocation.io/


Requirements
------------

This module requires the following modules:
python 3-alpine (at least)
Docker


Installation
------------

1.Create a folder in your project library called "Projec_NAME"
2.Copy the following files into your new folder:
	app.py
	Dockerfile
	docker-compose.yml
3.Open a terminal and cd (change directory) to the "Projec_NAME" folder
4.Make sure you are in the correct directory.
5.Run command: docker compose up
6.Open any browser and type: http://127.0.0.1/?ip={ip address}
7.Check that the Time-zone that appears really belongs to the IP Address you typed.



Creation proccess
------------
I used docker-compose in order to run my app on a container in Docker.
I used Docker Desktop for this task.


app.py-
This is a python script of a Flask server.
I used flask and requests packages to create a web server that will submit API requests from https://ipgeolocation.io/ to receive a Time-zone by IP.
I created my Flase server using a definition called get_location.
variable "ip" is a variable contatins an IP Address the application receives from the user
variable "timezone" contatins the result of the API GET request. I compressed it to format JSON.
changed variable "timezone" to contain only the "timezone: component received from my GET request.
I run my Flask server on host "0.0.0.0" (any IP) and port 5000 (Flasek default port)

First, I ran this code locally using PyCharm to make sure my flask server is running and that I receive the correct outcome.

Dockerfile-
I used Dockerfile to tell Docker what he needs to install.
I told the docker to use my Python app and copy the app.py file into the image being created.
I ran the following commands:
RUN pip install flask
RUN pip install requests
in order to install on my python the Flask and request packages.
using the CMD command I told Docker what command I want to run when my image is executed inside a container.

docker-compose.yml-
This Compose file is a YAML file defining services, networks, and volumes for the Docker application
I set a service named: "app"
build: . tells the Docker to use the image set in the current folder
I used port 80 to be the port of my app to ignore writing a diferent port in the url.
port 80 is my app port and I forward it to port 5000 of my flask server.







