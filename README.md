# ContactList "African Forest Elephant"
ContactList is a simple, configurable web application for managing comtact information. It is written in Python and makes use of the Django web framework. The project was inspired by the information management system that the character 'Dendy' uses in the cartoon series 'OK K.O. Let's Be Heroes', specifically the episode "I Am Dendy".

The codename was chosen in relation to how elephants have a great memory and how elephants are used to symbolize memory; the act of remembering something. 

ContactList is meant to be an "intermediate" project to CAMS, where a large amount of code from this project would be reused for that project. This is my first web application project that uses a database.

## Requirements

### Hardware (server)
ContactList may run on any platform that Python 3.8 and later supports, including but not limited to x86, x86-64, mips32, mips64, armv7l (32-bit, e.g. Raspberry Pi 2 and earlier, Banana Pi F2P/F2S) and armv8 (64-bit, e.g. Raspberry Pi 3 and 4). A minimum of **512MB of system memory (RAM) is recommended**. Depending on the environment, it may run on systems with less memory.

### Software (server)
ContactList is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows platforms is not guaranteed.

As Django 4.2 is currently the only dependency in "requirements.txt", the minimum Python version required is **3.8** as stated in the [Django documentation](https://docs.djangoproject.com/en/4.2/faq/install/).

### Software (client)
Due to the lack of login system and user settings at the moment, support for cookies is not required. HTML5 support is recommended. JavaScript may be required for some features.

## Setup
*Section To-Do*

## Configuration
The configuration file in config/database/entry.csv defines the form fields and database models used by the application. The included file is rather basic but can be modified to add more fields.

### When to use --build
./runner_dev can accept one command-line flag, --build

When --build is used, the script removes all of the built Python files, rebuilds such files and does any migrations. This may lead to data loss so it is recommended to back up the database before doing this.

When to use --build:

- After adding, removing or editing themes under config/themes/
- (Until dynamic models are implemented) After editing anything in config.json

*Rest of Section To-Do*
