# ContactList - CTCL 2023
# File: build.py
# Purpose: Management command for generating database models, form data and other files
# Created: June 9, 2023
# Modified: August 15, 2023

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
        perror("configthemes", "")


    return source


# Takes in a list of table configurations and returns the Python source
def configchoices(configjson, tables, themelist):


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
            print(f"build.py ERROR: config/config.json does not exist. Current working directory is \"{cwd}\".")
            sys.exit(1)
        except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
            print(f"build.py ERROR: Exception \"{e}\" raised by JSON library")
            sys.exit(1)

        # Collect themes from the "themes" directory
        themedir = [f for f in os.listdir("config/themes") if os.path.isdir(os.path.join("config/themes", f))]
        themelist = []
        for i in themedir:
            try:
                with open(f"config/themes/{i}/index.json") as f:
                    themedata = dict(json.load(f))["theme"]
                themelist.append(themedata)
            except FileNotFoundError:
                print(f"build.py theme loader WARNING: Theme \"{i}\" does not have a index.json, the theme would not be available")
            except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
                print(f"build.py theme loader WARNING: Exception \"{e}\" raised by JSON library, the theme would not be available")

        if len(themelist) < 1:
            print(f"build.py theme loader ERROR: No themes were found in the directory config/themes/")
            sys.exit(1)

        res_configthemes = configthemes(themelist)
        res_configchoices = configchoices(configjson, themelist)
        res_configmodels = configmodels(configjson)
        res_configfields = configfields(configjson)

        #with open("themecfg.json", "w") as f:
        #    f.write(res_configthemes)

        #with open("contactlist/choices.py", "w") as f:
        #    f.write(res_configchoices)

        #with open("contactlist/models.py", "w") as f:
        #    f.write(res_configmodels)

        #with open("contactlist/fields.py", "w") as f:
        #    f.write(res_configfields)