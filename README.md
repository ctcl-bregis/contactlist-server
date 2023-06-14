# ContactList
ContactList is a simple, configurable web application for managing comtact information. It is written in Python and makes use of the Django web framework.

## Requirements

### Hardware (server)
ContactList may run on any platform that Python 3 supports, including but not limited to x86, x86-64, mips32, mips64, armv7l (32-bit, e.g. Raspberry Pi 2, Banana Pi F2P/F2S and earlier) and armv8 (64-bit, e.g. Raspberry Pi 3 and 4). A minimum of **512MB of system memory (RAM) is recommended**. Depending on the environment, it may run on systems with less memory.

### Software (server)
ContactList is developed entirely on Debian GNU/Linux and Linux Mint. Functionality on Windows platforms is not guaranteed.

As Django 4.2 is currently the only dependency in "requirements.txt", the minimum Python version required is **3.8** as stated in the [Django documentation](https://docs.djangoproject.com/en/4.2/faq/install/).

### Software (client)
Due to the lack of login system at the moment, support for cookies is not required. Also, JavaScript is not required to use the features of the web application. HTML5 support is recommended.
