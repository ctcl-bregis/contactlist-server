## 0.6.0 - [UNRELEASED] - Production Update
So far this is the largest update yet by code size.

Additions:

- Added Sass for styling due to its use with Bootstrap
- Added the Integrated Documentation feature of CAMS into ContactList
- Addition of markdown editor fields, along with the new datatype "mdtext"
- Addition of CardDAV sync support
- Multiple database table support though unused by ContactList. This resulted in the rewrite of the build.py management command

Changes:

- Action buttons are now within a single table cell instead of each button having it's own cell, this change is reflected in config.json
- Automatic setting of the "theme" cookie to the default Flat Dark theme to avoid having "lib.py WARNING: Theme "None" not found, using default" being printed every time a page is loaded when there is no theme cookie set.
- Indentation fixes in config.json
- Management command genmodels.py renamed to build.py to better describe its function
- General code optimizations
- Total rewrite of themes with the introduction of Bootstrap

## 0.5.2 - July 18, 2023 - Mobile-Friendy Update

Changes:

- Code optimizations

Fixes:

- CSS fixes specific to having the application more usable on phones and other vertical displays

## 0.5.1 - July 5, 2023 - Chromebook Hotfix

Fixes:

- Search feature now searches for content in TextField objects/textarea

Called "Chromebook Hotfix" since it was discovered and fixed from a Chromebook

## 0.5.0 - July 4, 2023 - Browser Update

Additions:

- Search feature
- Form categories
- CSS minification for themes

Changes:
- The navigation bar no longer has a separate configuration file and is now part of config.json
- choices.py now consists of a single dictionary definition instead of a list of tuples for each dropdown fieldcontactlist/management/commands/build.py
- Dropdown choices in config.json are now stored in a dictionary instead of a list of lists

Fixes:

- Social media platform is properly displayed under "View"
- Better error handling in genmodels
- JQuery is now loaded only when it is needed
- tablesorter is now loaded only when it is needed
- Font Awesome icons are now loaded only when it is needed
- CSS cleanup
- CSS fixes

## 0.4.2 - June 29, 2023 - Time fix

Fixes:

- Fixed strftime string
- CSS fixes

## 0.4.1 - June 28, 2023 - More Data?

Additions:

- More table fields in config.json
- More social platforms added to the dropdown

Fixes:

- Removed unused "name" fields from table configuration in config.json
- Fixed paths for tablesorter static files
- CSS fixes

## 0.4.0 - June 28, 2023 - Sorting Update

Added:

- Added [tablesorter](https://mottie.github.io/tablesorter/) along with JQuery for the main page table, allowing fields to be sorted
- Confirmation for deleting items
- Ability to export all data as a CSV file

Fixes:

- Added mkcontext to lib.py for pre-filling the dictionary passed as the context for templates. This can make debugging code easier.

## 0.3.0 - June 23, 2023 - Font Awesome update

Added:

- Added fontawesomefree as a pip requirement
- Font Awesome icons can now be used for button icons

Fixes:

- Fixed OSError Input/Output Error being raised from trying to call print() when the server is running headless

## 0.2.1 - June 22, 2023 - Theme switcher fix

Fixes:

- Fixed theme function not returning anything if a theme is not found or is not defined, resulting in an internal server error

## 0.2.0 - June 22, 2023 - "Don't let it overcharge!"

Changes:

- Better configuration of the list page table
- Added navbar, where "Add Contact" is now located

Additions:

- Implemented theme switcher

## 0.1.0 - June 16, 2023 - "Put that down, it's a prototype"

First release of ContactList, where it would be field-tested by being used on my servers for personal contact management. In the app's current state, it may be unstable and have unimplemented features.

This release was done from Fort Myers Beach, Florida, United States on a follow-up business trip.