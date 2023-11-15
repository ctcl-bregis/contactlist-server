# ContactList - CTCL 2023
# File: lib.py
# Purpose: Commonly used functions, similar to lib.rs in Rust
# Created: June 7, 2023
# Modified: November 15, 2023

from datetime import datetime, timezone
import json, base64
from os import listdir
from os.path import isdir, join, exists
from . import __version__

# printe statement that does not raise an exception if the code is running headless
def printe(text):
    try:
        print(text)
    except OSError:
        pass

# Load the config on startup instead of every time a function needs it
if exists("config/config.json"):
    try:
        with open("config/config.json") as f:
            gconfig = json.loads(f.read())["config"]
    except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
        printe(f"lib.py ERROR: Exception \"{e}\" raised by JSON library")
else:
    printe(f"lib.py ERROR: Global configuration at config/config.json does not exist")

if exists(gconfig["table"]):
    try:
        with open(gconfig["table"]) as f:
            tconfig = json.loads(f.read())["table"]
    except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
        printe(f"lib.py ERROR: Exception \"{e}\" raised by JSON library")
else:
    printe(f"lib.py ERROR: Global configuration at {gconfig['table']} does not exist")

if exists(gconfig["themes"]["themecfg_path"]):
    try:
        with open(gconfig["themes"]["themecfg_path"]) as f:
            themes = json.loads(f.read())
    except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
        printe(f"lib.py ERROR: Exception \"{e}\" raised by JSON library")
else:
    printe(f"lib.py ERROR: Theme configuration at {gconfig['themes']['themecfg_path']} does not exist")


# Get a specific key from the global configuration file
def getgconfig(part):
    try:
        return gconfig[part]
    except KeyError:
        printe(f"lib.py WARNING: Key \"{part}\" does not exist in config/config.json")
        return None

# Get a specific key from the table configuration file
def gettconfig(part):
    try:
        return tconfig[part]
    except KeyError:
        printe(f"lib.py WARNING: Key \"{part}\" does not exist in {gconfig['themes']['themecfg_path']}")
        return None


# Timestamp to formatted date
def dt2fmt(dt):
    strfstr = getgconfig("global")["strftime"]

    return dt.strftime(strfstr)

# "Human size" data size formatting
def hsize(fsize):
    suffix = "Bytes"

    for unit in [" ", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(fsize) < 1024.0:
            return f"{fsize:3.0f} {unit}{suffix}"
        fsize /= 1024.0

    return f"{num:.1f} Yi{suffix}"

if exists(gconfig["themes"]["themecfg_path"]):
    with open(gconfig["themes"]["themecfg_path"]) as f:
        themes = json.loads(f.read())
else:
    printe("lib.py ERROR: {gconfig['themes']['themecfg_path']} does not exist, it may not have been generated yet")
    themes = {}

# Return theme data
def gettheme(tname):
    try:
        return themes[tname]
    except KeyError:
        printe(f"lib.py WARNING: Theme \"{tname}\" not found, using default")
        try:
            return themes["default"]
        except:
            printe(f"lib.py WARNING: Default theme does not exist, styling may be unavailable")
            return ""


# Function to prefill context data to make views smaller
def mkcontext(request, title, scripts=""):
    themecookie = gettheme(request.COOKIES.get("theme"))

    context = {
        "title": title,
        "misc": getgconfig("misc"),
        "navbar": getgconfig("navbar"),
        "ver": __version__,
        "appname": getgconfig("global")["appname"],
        "dev": getgconfig("global")["dev"]
    }

    context["styling"] = themecookie

    if themecookie != "":
        context["bsparams"]: themecookie["bootstrap"]
    else:
        context["bsparams"]: "dark"

    # font - Load just fontawesome
    # form - Load JQuery and Select2
    # table - Load JQuery, fontawesome and tablesorter
    if scripts == "font":
        context["fa"] = True
        context["jq"] = False
        context["ts"] = False
        context["s2"] = False
    elif scripts == "form":
        context["fa"] = False
        context["jq"] = True
        context["ts"] = False
        context["s2"] = True
    elif scripts == "table":
        context["fa"] = True
        context["jq"] = True
        context["ts"] = True
        context["s2"] = False
    else:
        context["fa"] = False
        context["jq"] = False
        context["ts"] = False
        context["s2"] = False

    return context

