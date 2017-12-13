# A Cookiecutter for Girder Worker Task Plugins

This repository contains a [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) for creating a [Girder Worker task plugin](http://girder-worker.readthedocs.io/en/latest/developer-docs.html#writing-your-own-plugin) - that is, a plugin that adds custom tasks to Girder Worker. The cookiecutter provides boilerplate code for creating an installable python package which Girder Worker will be able to discover.


## Installation

First you must [install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html). Then simply run cookiecutter where you would like to create your custom task plugin. 

```
cookiecutter https://github.com/girder/cookiecutter-gw-plugin.git
```

This will prompt you for a number of template variables such as ```plugin_slug```, ```author_name```, etc.  Once complete, cookiecutter will create a directory with the same name you provided for ```plugin_slug``` (by default gw_task_plugin). 

___Remember___ this is just boilerplate code.  Please explore the package files for ```TODO``` comments that describe things to do once you've generated your plugin. 

## Template Variables

The Girder Worker Task Plugin Cookiecutter has several template variables that are used throughout the boilerplate code.

+ *author_name* - The name of the package author. Used in setuptools' package metadata.
+ *email* - The email of the package author. Used in setuptools' package metadata.
+ *plugin_name* - The human readable name of the plugin.  Used in documentation strings, package metadata.
+ *plugin_slug* - The name of the python package (e.g.  ```pip install plugin_slug```).
+ *plugin_camel* - A camel case version of the plugin_slug.  Used for certain internal classes.
+ *plugin_short_description* - A short description of the plugin's purpose. Used in setuptools' package metadata.
+ *version* - The version of the package. (Defaults to 0.0.0).
+ *open_source_license* - The type of license for the plugin. Used in setuptools' package metadata.
