# ContactList - CTCL 2023
# Date: May 4, 2023 (Reused from CAMS) - June 28, 2023
# Purpose: Commonly used functions, similar to lib.rs in Rust

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
with open("config/config.json") as f:
    jsondata = json.loads(f.read())

themes = {}

themedir = [f for f in listdir("config/themes") if isdir(join("config/themes", f))]
for i in themedir:
    tdata = {}
    try:
        with open(f"config/themes/{i}/index.json") as f:
            jdata = dict(json.load(f))
        
        temppath = jdata["theme"]["css"]
        if temppath != "":
            try:
                with open(f"config/common/base.css") as f:
                    tdata["styling"] = f.read()
            except FileNotFoundError:
                printe(f"lib.py WARNING: config/common/base.css does not exist")
                
            try:
                with open(f"config/themes/{i}/{temppath}") as f:
                    tdata["styling"] += f.read()
            except FileNotFoundError:
                printe(f"lib.py WARNING: config/themes/{i}/{temppath} does not exist")
        else:
            printe(f"lib.py WARNING: Styling path is blank in theme \"{i}\", ignoring")
            tdata["themecss"] = ""
        
        temppath = jdata["theme"]["logo"]
        if temppath != "":
            try:
                with open(f"config/themes/{i}/{temppath}") as f:
                    tdata["logo"] = "data:image/svg+xml;base64," + base64.b64encode(f.read().encode("utf-8")).decode("utf-8")
            except FileNotFoundError:
                printe(f"lib.py WARNING: config/themes/{i}/{temppath} does not exist")
        else:
            printe(f"lib.py WARNING: Logo path is blank in theme \"{i}\", ignoring")
            tdata["logo"] = ""
        
        temppath = jdata["theme"]["tstheme"]
        if temppath != "":
            # TODO: Detect if the theme file exists
            if temppath["file"].startswith("/static/"):
                tdata["tstheme"] = temppath
            else:
                printe(f"lib.py WARNING: tablesorter theme path is invalid: \"{temppath['file']}\". Defaulting to /static/tablesorter/css/theme.default.min.css")
                tdata["tstheme"] = {"file": "/static/tablesorter/css/theme.default.min.css", "name": "default"}
        else:
            printe(f"lib.py WARNING: tablesorter theme is blank. Defaulting to /static/tablesorter/css/theme.default.min.css")
            tdata["tstheme"] = {"file": "/static/tablesorter/css/theme.default.min.css", "name": "default"}
        
        themes[i] = tdata
    except FileNotFoundError:
        printe(f"lib.py WARNING: Theme \"{i}\" does not have a index.json, it would not be available")
        pass

# Get a specific part/key of the config
def getconfig(part):
    try:
        return jsondata["config"][part]
    except KeyError:
        printe(f"lib.py WARNING: Key \"{part}\" does not exist in config/config.json")
        return None

# Timestamp to formatted date
def dt2fmt(dt):
    # TODO: have strfstr read from a config file
    strfstr = getconfig("misc")["strftime"]

    return dt.strftime(strfstr)

# "Human size" data size formatting
def hsize(fsize):
    suffix = "Bytes"
    
    for unit in [" ", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(fsize) < 1024.0:
            return f"{fsize:3.0f}{unit}{suffix}"
        fsize /= 1024.0
        
    return f"{num:.1f}Yi{suffix}"
   
# Active page, cfgpath has a default value that can be overridden
def navbar(active = "", cfgpath = "config/navbar.json"):
    with open(cfgpath) as f:
        jdata = dict(json.load(f))
        
    return jdata

# Return theme data
def theme(tname):
    try:
        return themes[tname]
    except KeyError:
        printe(f"lib.py WARNING: Theme \"{tname}\" not found, using default")
        return themes["default"]
        
# Function to prefill context data to make views smaller
def mkcontext(request, title):
    context = {"title": title, "styling": theme(request.COOKIES.get("theme")), "misc": getconfig("misc"), "navbar": navbar, "ver": __version__}
    return context
    
    
    
        
