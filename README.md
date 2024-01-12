# ContactList "Brown Trout"

ContactList is a simple, configurable web application for managing comtact information. It is written in Python and makes use of the Django web framework. 

ContactList is meant to be an "intermediate" project to CAMS, where a large amount of code from this project would be reused for that project. This is my first web application project that uses a database.

## Requirements

### Software (server)
ContactList is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows platforms is not guaranteed.

As Django 5.0 is currently the only dependency in "requirements.txt", the minimum Python version required is **3.8** as stated in the [Django documentation](https://docs.djangoproject.com/en/4.2/faq/install/).

### Software (client)
Due to the lack of login system and user settings at the moment, support for cookies is not required. HTML5 support is recommended. JavaScript may be required for some features.


The support for specific browsers is currently defined by the application's use of Boostrap, its requirements as listed in [the documentation](https://getbootstrap.com/docs/5.3/getting-started/browsers-devices/#supported-browsers) are as follows:

Chrome 60 or later
Firefox 60, ESR, or later
iOS 12 or later
Safari 12 or later

ContactList is however mainly tested within Chromium and other browsers may be untested.

## Setup
*Section To-Do*

## Configuration
*Section To-Do*

### When to use --build
./runner_dev can accept one command-line flag, --build

When --build is used, the script removes all of the built Python files, rebuilds such files and does any migrations. This may lead to data loss so it is recommended to back up the database before doing this.

When to use --build:

- After adding, removing or editing themes under config/themes/
- (Until dynamic models are implemented) After editing anything in config.json

*Rest of Section To-Do*

## Dependencies

### Bootstrap
Bootstrap is included with the app under "app/static/bootstrap/" in compressed form. Its license can be found at "app/static/bootstrap/LICENSE".

### jQuery
jQuery is included with the app under "app/static/jquery/" in compressed form. Its license can be found at "app/static/jquery/LICENSE".

### tablesorter
tablesorter is included with the app under "app/static/jquery/" in compressed form. Its license can be found at "app/static/tablesorter/LICENSE".