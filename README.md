![project cover](.static/cover.jpg)

# NutApp

[![Coverage](https://codecov.io/gh/claudinoac/nutapp/branch/master/graph/badge.svg)](https://codecov.io/gh/claudinoac/nutapp)
![Deploy](https://github.com/claudinoac/nutapp/workflows/Deploy/badge.svg)
![Tests](https://github.com/claudinoac/nutapp/workflows/Tests/badge.svg?branch=dev)
![Security Checks](https://github.com/claudinoac/nutapp/workflows/Security/badge.svg?branch=dev)
![Lint](https://github.com/claudinoac/nutapp/workflows/Lint/badge.svg?branch=dev)
[![PyPI version](https://badge.fury.io/py/nutapp.svg)](https://badge.fury.io/py/nutapp)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Template for production-ready django-based applications

Featuring:


- Django 4+
- Quasar 2+ w/ Vite
- Container runtime


## Table of Contents:


- [Installation](#installation)
- [Project Architecture](#architecture)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Installation:

### Requisites:
- Install [docker](https://www.docker.com/products/docker-desktop) and [docker-compose](https://docs.docker.com/compose/install/)


### Clone:

- Clone this repository:
	- ` git clone git@github.com:claudinoac/nutapp`

### Setup:

- Build and run containers:
	+ ```$ docker-compose up -d```


- Access [http://localhost:7200](http://localhost:7200')

- The ui and the server will be up and listening for file changes. 

---

## Architecture:

### Package Diagram

![package diagram](.static/package_diagram.png)

---

## Testing:


### Unit tests:

- The unit tests are based on [Django test suite](https://docs.djangoproject.com/en/4.0/topics/testing/)
	
- All the unit tests should be located in apps/app_name/tests/unit/ 
- To run the unit tests, run 
	- ```$ make run-unit-tests```


## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/claudinoac/nutapp.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/claudinoac/nutapp/compare/" target="_blank">`https://github.com/claudinoac/nutapp/compare/`</a>.

---

## Team

### Maintainers:
| <a href="http://github.com/claudinoac" target="_blank">**Alisson Claudino**</a>|
| :---: |
| [![Alisson Claudino](https://avatars3.githubusercontent.com/u/23270841?s=200&v=4)](http://fvcproductions.com)  |
| <a href="http://github.com/fvcproductions" target="_blank">`github.com/claudinoac`</a> |

### Contributors:
---

## FAQ

- **How can I change my api configs?**
    - In the backend/NutApp/settings/(development|production).py

---

## Support

Reach us out at one of the following places!

- Twitter at <a href="http://twitter.com/_claudinoac" target="_blank">`@_claudinoac`</a>

---

## License

- **[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**


