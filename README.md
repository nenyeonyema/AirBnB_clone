# Airbnb Clone Project
Welcome to our Airbnb Clone project! This project aims to replicate the core functionality of the popular accommodation rental platform Airbnb. Whether you're a developer looking to
contribute or a user interested in trying out our application, this README.md file will guide you through the setup and usage of our Airbnb Clone.

## AirBnB Clone Command Interpreter
### Description:
The AirBnB Clone Command Interpreter is a tool that allows users to interact with the system by entering commands through a text-based interface. In this simplified version, the focus is on managing information about people. The command interpreter enables users to create, update, and delete records of individuals, as well as list all the people in the system. Additionally, it provides functionality to save and load data to and from a file.

## How to Start It:
Clone the Repository:

Clone the AirBnB Clone repository to your local machine.
### bash
git clone https://github.com/your-username/AirBnB_clone.git
Navigate to the Project Directory:

Change into the project directory.

### bash
cd AirBnB_clone
Run the Command Interpreter:

Start the command interpreter by running the console.py script.

### bash
python console.py
## How to Use It:
## The command interpreter provides various commands for managing people records. Here are the available commands and their usage:

### Create a Person:

Syntax: create <name> <age>
Example: create Alice 30
This command adds a new person with the specified name and age to the system.

### Update a Person:

Syntax: update <index> <attribute> <value>
Example: update 0 name Jane
This command updates the specified attribute (e.g., name) of the person at the given index.

### Destroy a Person:

Syntax: destroy <index>
Example: destroy 1
This command removes the person at the specified index from the system.

### List All People:

Syntax: list
Example: list
This command displays a list of all people in the system, including their names and ages.

### Save to a File:

Syntax: save <filename>
Example: save data.json
This command saves the current data (people records) to a JSON file with the specified filename.

### Load from a File:

Syntax: load <filename>
Example: load data.json
This command loads data from a previously saved JSON file, restoring the system's state.

### Exit the Console:

Syntax: exit
Example: exit
This command exits the command interpreter, ending the session.

### Examples:

>> create Alice 30
>> create Bob 22
>> list

Output:
json
[
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 22}
]

>> update 0 name Jane
>> destroy 1
>> list

Output:
json
[
  {"name": "Jane", "age": 30}
]
>> save data.json
>> exit
This sequence of commands saves the current data to a file named "data.json" and exits the command interpreter.

## Contributors

Chinenye Genevieve Onyema <br>
Oluwatobiloba Ojo

## Acknowledgments
Appreciation goes ALX Software Engineers for the learning opportunity and engaging projects.
Thanks to the creators of Airbnb for inspiring this project.
Special thanks to us the contributors for our valuable efforts.
Built with ❤️ and ☕️.
