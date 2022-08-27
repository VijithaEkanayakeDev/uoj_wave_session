# University of Jaffna - H2O Wave hands on exercise

This repository contains set of basic wave examples that anyone that start development of interacting applications using H2O wave.

## Running and trying out the examples

### System Requirement

1. Python 3.7+
2. pip3

## Install h2o_wave library

To setup the environment to wave application development execute below command. This basically creates a python virtual environment for your development, activates it and finally install h2o_wave library to be used for the wave app development.
```shell
python3 -m venv venv
source ./venv/bin/activate
./venv/bin/pip install h2o-wave
```

### Trying out the examples

#### hello world app
To run hello world example execute following command in the command line.
```shell
./venv/bin/wave run hello_world.py
```
Once you run this command, It will start the wave server and hello world wave application. It will create card with content of Hello World. You can access the application by navigating to [http://localhost:10101/ ](ttp://localhost:10101/ )

#### publish content to wave page via wave scripts
```shell
./venv/bin/wave run hello_world.py
```
Once you run this command, It will start the wave server and hello world wave application. It will create card with content of Hello World.
In another terminal, run script.py to publish the content to wave server.

```shell
./venv/bin/python3 script.py
```

You can access the application by navigating to [http://localhost:10101/ ](ttp://localhost:10101/ )


#### basic user interaction app

To run try out basic user interaction example execute following command in the command line.
```shell
./venv/bin/wave run basic_user_interaction.py
```
You can access the application by navigating to [http://localhost:10101/ ](ttp://localhost:10101/ )


#### routing example

To run try out basic routing example execute following command in the command line.
```shell
./venv/bin/wave run basic_routing.py
```
You can access the application by navigating to [http://localhost:10101/ ](ttp://localhost:10101/ )

H2O Wave has very rich documentation which covers all of these concepts. Documentation is available [here](https://wave.h2o.ai/)
