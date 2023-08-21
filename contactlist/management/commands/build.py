# ContactList - CTCL 2023
# File: build.py
# Purpose: Management command for generating database models, form data and other files
# Created: June 9, 2023
# Modified: August 21, 2023

import json
import os
import platform
import shutil
import sys
from datetime import datetime, timezone
from csscompressor import compress
from django.core.management.base import BaseCommand, CommandError
from scss import Compiler

# Function that keeps error messages consistent
def perror(func, message):
    print(f"build.py {func} ERROR: {message}")
    sys.exit(1)

# Same function as perror but it does not exit
def pwarn(func, message):
    print(f"build.py {func} WARNING: {message}")

# Collect themes from the "themes" directory
def themeloader(themeconfigdir):
    themedir = [f for f in os.listdir(themeconfigdir) if os.path.isdir(os.path.join(themeconfigdir, f))]
    themelist = []
    for i in themedir:
        try:
            with open(f"{themeconfigdir}{i}/index.json") as f:
                themedata = dict(json.load(f))["theme"]
                themelist.append(themedata)
        except FileNotFoundError:
            perror("themeloader", f"Theme does not have a index.json, the theme \"{i}\" would not be available")
        except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
            perror("themeloader", f"Exception \"{e}\" raised by JSON library, the theme \"{i}\" would not be available")

    # Exit the script if there are no themes
    if len(themelist) < 1:
        perror("themeloader", f"No themes were found in the directory {themeconfigdir}")

    return themelist

# Load configuration for each defined table
def tableloader(configjson):
    tables = {}
    for cfgtable in configjson["tables"]:
        # Is the "important" key set to "True"? If the config has this table with the "important" set to "True", the app will not run without it.
        if cfgtable["important"] == "True":
            important = True

        table = {}
        # What is appended to for each class name
        prefix = cfgtable["classprefix"]
        with open(cfgtable["cfg"]) as f:
            tableconfig = json.loads(f.read())["table"]

        # Assign the tableconfig dictionary to table as many of the same values are used
        table = tableconfig

        table["choicesclass"] = prefix + "Choices"
        table["modelclass"] = prefix + "Item"
        table["fieldsclass"] = prefix + "Field"

        keys = ["headers", "tablecats", "table", ]
        for key in keys:
            if not key in table:
                if important:
                    perror("tableloader", f"Key {key} missing from the configuration table.")
                else:
                    pwarn("tableloader", f"Key {key} missing from the configuration table. The table config \"{prefix}\" would be unavailable.")
                    break
        else:
            # This should be the last assignment in the for loop
            tables[prefix] = table

    return tables

# Takes in a list of dictionaries containing theme data and returns the JSON source
def configthemes(configjson, themelist):
    basescsspath = configjson["misc"]["basescss"]

    if os.path.exists(basescsspath) and os.path.isfile(basescsspath):
        with open(configjson["misc"]["basescss"]) as f:
            basescss = f.read()
            try:
                basecss = Compiler().compile_string(basescss)
            except Exception as err:
                perror("configthemes", "Sass compilation error when processing base.scss: {err}")
    elif os.path.exists(basescsspath) and not os.path.isfile(basescsspath):
        perror("configthemes", "\"{basescsspath}\" is not a file")
    else:
        perror("configthemes", "\"{basescssfile}\" does not exist")

    for theme in themelist:
        themedict = {}
        try:
            theme["css"] = Compiler().compile_string(theme["scss"])
        except Exception as err:
            pwarn("configthemes", f"Sass compilation error while processing theme \"{theme['int_name']}\": {err}")

        themedict[theme["int_name"]] = theme

    source = json.dumps(themedict)

    return source


# Takes in a list of table configurations and returns the Python source
def configchoices(configjson, tables, themelist):
    for table in tables:
        print(table)
    

    return source

# Takes in a list of table configurations and returns the Python source
def configmodels(configjson, tables):
    
    return source


def configfields(configjson, tables):

    return source


class Command(BaseCommand):
    help = "Generates all of the needed files for the application."
    cwd = os.getcwd()

    def handle(self, *args, **options):
        # Create a backup of the database since migrations may wipe the data
        if os.path.exists("db.sqlite3"):
            if os.path.exists("db_backup.sqlite3"):
                os.remove("db_backup.sqlite3")
            shutil.copyfile("db.sqlite3", "db_backup.sqlite3")

        # Get global config
        try:
            with open("config/config.json") as f:
                configjson = json.loads(f.read())["config"]
        except FileNotFoundError:
            perror("config loader", "config/config.json does not exist. Current working directory is \"{cwd}\".")
        except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
            perror("config loader", "Exception \"{e}\" raised by JSON library")

        themelist = themeloader("config/themes/")
        res_configthemes = configthemes(configjson, themelist)

        tables = tableloader(configjson)

        res_configchoices = configchoices(configjson, tables, themelist)
        res_configmodels = configmodels(configjson, tables)
        res_configfields = configfields(configjson, tables)

        #with open("themecfg.json", "w") as f:
        #    f.write(res_configthemes)

        #with open("contactlist/choices.py", "w") as f:
        #    f.write(res_configchoices)

        #with open("contactlist/models.py", "w") as f:
        #    f.write(res_configmodels)

        #with open("contactlist/fields.py", "w") as f:
        #    f.write(res_configfields)