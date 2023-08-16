## "config/"
The "config/" directory contains all of the configuration files for the application.

Currently these directories and one file exist under "config/":

- config.json
- docs/
- tables/
- themes/

### "config/config.json"
"config/config.json" is a JSON configuration file at the "root" of the configuration directory. It stores configuration information for use o

#### "misc"
The "misc" key stores miscellaneous configuration data for certain purposes:

Currently, as of 0.6.0, these keys exist under "misc":

- "logotext": The text used in case a "Logo" is to be shown in the navigation bar
- "basescss": Path realitive to the application root to the file that stores the common styling data that is added to every theme
- "facssurl": Realitive URL to the compiled CSS file for Font Awesome icons
- "fajsurl": Realitive URL to the compiled JavaScript file for Font Awesome icons
- "bscssurl": Realitive URL to the compiled CSS file for Bootstrap
- "bsjsurl": Realitive URL to the compiled JavaScript file for Bootstrap
- "jqurl": Realitive URL to the compiled JavaScript file for JQuery
- "tsurl": Realitive URL to the compiled JavaScript file for tablesorter

Files for Bootstrap, tablesorter and JQuery ship with the app and are located under "static/". Only the compiled/minimized version of these files come with the app. The license texts are within the directories of each included library.

Files for django-markdownx and Font Awesome are included as PyPi packages and are installed with the command <code>pip install -r requirements.txt</code>.

#### "global"
The "global" key stores data that is used by almost every page. It is for configuration that is considered more important than what is under "misc".

Currently, as of 0.6.0, these keys exist under "global":

- "strftime": The string to use for formatting datetime timestamp objects. This string is used wherever a timestamp is displayed to the user.
- 

#### "tables"
Files that define what tables are available to the app, 

#### "htmltable"
"htmltable" is the key for storing what data is shown by the table on the Main page and Search Results page. The key stores a list of dictionaries.

##### "type": "info"
Any table column with the type "info" shows the specified database table entry

The specific parameters for a dictionary with the "type" key set to "info" are:

- "db": Database table to get the data from, this is the name of the class in models.py. An example would be "ContactItem"
- "col": This is the specific column of a row to get the data from. The value to use here is the four-letter column name, for example: "name". This also determines what header is displayed at the top of a row

### "config/docs/"
The subdirectory "config/docs/" is for all of the files shown in the Integrated Documentation feature. The Documentation page shows a file browser-like interface with "config/docs/" as the "root" directory.

All files are shown in directory file lists, though supported files or directories are viewable and have a link. Attempts to view a page of a unsupported file would simply return an HTTP 404 error.

Supported file extensions are defined by the "knowntypes" dictionary in the "docs" section of "config/config.json".

### "config/tables/"
The subdirectory "config/tables/", new with ContactList 0.6.0, is a directory for storing configuration information of the database tables, forms,

### "config/themes/"
The subdirectory "config/themes/" is for storing themes. A valid theme with the directory name "default" is required. If it does not exist or is invalid, errors may occur.

There is one styling file named "base.scss", this is the base styling information and it is appended to the beginning of a theme's styling data after compilation.