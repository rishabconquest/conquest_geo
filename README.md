## Conquest QGIS plugin

This is the Conquest QGIS plugin, created as a prototype for our initial Public API <-> GIS integrations.

It is written in Python3 and uses Qt (PyQt) to build xml forms.

The product is distributed through a .zip file to customers who want to install it on their QGIS app:

    `Plugins > Manage and Install Plugins ... > Install from ZIP`

## What it provides

A task to add a selected Geometry to Conquest as a new asset. 

The task is accessible using the Conquest tick icon in the toolbar or under the `Plugins > Conquest` menu

## Bundling the plugin on Windows

You will need python and make installed on your machine. Use the scoop package manager:

```
scoop install make
scoop install python
```

Using `pip` the python package manager tool, install the requirements for this project by running:

```
pip install -r requirements.txt
```

At this point you can use the build tool to create the .zip file that is installed in the QGIS app.

```
pb_tool zip
```

The zip file is available at: `./zip_build/conquest_geo.zip`

## Bundling the plugin on a posix system

`make clean; find . -exec touch {} \; ; make compile ; find . -exec touch {} \; ; make zip;`

## A little about the development process

When QGIS installed (using 3.24 at the time of dev) plugins are installed under the folder:

`~\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\conquest_geo`

You can modify code directly under this directory for a quicker feedback loop.

For UI development, there is a QT designer.exe for the .ui files which is available from the `qt5_applications` package.

You can install this package using a "Virtual Python ENV" and look inside the `.\venv\Lib\site-packages\qt5_applications\Qt\bin` folder

## Obtaining the Conqeust Public API client library

> Currently the current version from [github.com/ConquestSolutions/python-conquest](https://github.com/ConquestSolutions/python-conquest) 
> is copied under the `./vendor` folder.

There is also a package that has been pushed to PyPI that can be used here [conquest](https://pypi.org/project/conquest/) installable using

`pip install conquest`

## More on QGIS plugin development

See [QGIS documentation](https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/index.html)

