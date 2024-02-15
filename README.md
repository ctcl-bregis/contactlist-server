# ContactList "Brown Trout"

ContactList is a simple, configurable web application for managing contact information. It is written in Python and makes use of the Django web framework. 

ContactList is meant to be an "intermediate" project to CAMS, where a large amount of code from this project would be reused for that project. This is my first web application project that uses a database.

## Requirements

### Software (server)
ContactList is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows, Mac and BSD platforms is not guaranteed.

Dependencies for front-end code such as Bootstrap and jQuery are installed with npm and are automatically copied to "app/static".

Python dependencies are installed with pip.

### Software (client)
Due to the lack of login system and user settings at the moment, support for cookies is not required. HTML5 support is recommended. JavaScript may be required for some features.

The support for specific browsers is currently defined by the application's use of Boostrap, its requirements as listed in [the documentation](https://getbootstrap.com/docs/5.3/getting-started/browsers-devices/#supported-browsers) are as follows:

Chrome 60 or later
Firefox 60, ESR, or later
iOS 12 or later
Safari 12 or later

ContactList is almost always tested with Chromium and other browsers may be untested.

## Setup
Ensure that npm, python3-pip and python3 are installed on the server.

*Section To-Do*

## Configuration
*Section To-Do*

### When to use --build
./runner_dev and ./runner_prod can accept one command-line flag, --build

When --build is used, the script removes all of the built Python files, rebuilds such files and does any migrations. This may lead to data loss so it is recommended to back up the database before doing this.

When to use --build:

- After adding, removing or editing themes under config/themes/
- (Until dynamic models are implemented) After editing anything in config.json

*Rest of Section To-Do*

