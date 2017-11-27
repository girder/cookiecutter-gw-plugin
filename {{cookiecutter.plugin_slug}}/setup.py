from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_desc = fh.read()


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(name='{{ cookiecutter.plugin_slug }}',
      version='{{ cookiecutter.version }}',
      description='{{ cookiecutter.plugin_short_description }}',
      long_description=long_desc,
      author='{{ cookiecutter.author_name }}',
      author_email='{{ cookiecutter.email }}',
{%- if cookiecutter.open_source_license in license_classifiers %}
      license="{{ cookiecutter.open_source_license }}",
{%- endif %}
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
{%- if cookiecutter.open_source_license in license_classifiers %}
          '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
          'Topic :: Scientific/Engineering',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python'
      ],
      install_requires=[
          "girder_worker",
          "girder_worker_utils"
          # TODO: Add additional packages required by both
          # producer and consumer side installations
      ],
      extras_require={
          "girder": [
              # TODO: Add dependencies here that are required for the
              # package to work on the producer (Girder) side.
          ],
          "worker": [
              # TODO: Add dependencies here that are required for the
              # package to work on the consumer (Girder Worker) side.
          ]
      },
      include_package_data=True,
      entry_points={
          'girder_worker_plugins': [
              '{{ cookiecutter.plugin_slug }} = {{ cookiecutter.plugin_slug }}:{{ cookiecutter.plugin_camel }}',
          ]
      },
      packages=find_packages(),
      zip_safe=False)
