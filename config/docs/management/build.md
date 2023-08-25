"build.py" is a management command included with ContactList. It reads certain configuration files within the "config/" directory.

It is called by the "runner_dev" BASH script using the command "python3 -B manage.py build" in the project root. If the command returns a non-zero exit code, either by a uncaught Python exception or is returned by the script by an implemented error, the script would exit, in an attempt to prevent data loss. See runner_dev.md in the same documentation directory as this file.

## Functions
This covers the actual Python functions that are responsible for generating each file.

In build.py, these functions are called and the returned string is written directly to each respective file.

### configthemes
configthemes is the function used first, it takes in a list of themes and tries to generate a JSON dump containing all of the data for each theme.


### configchoices
configchoices generates the contents of the choices.py file under "contactlist/"


### configmodels
Along with the tables defined by configuration files, some other tables are generated.

