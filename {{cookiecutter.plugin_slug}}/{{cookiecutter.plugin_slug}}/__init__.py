# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.plugin_name }}."""

__author__ = """{{ cookiecutter.author_name}}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


from girder_worker import GirderWorkerPluginABC


class {{ cookiecutter.plugin_camel }}(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def task_imports(self):
        # Return a list of python importable paths to the
        # plugin's path directory
        return ['{{ cookiecutter.plugin_slug }}.tasks']
