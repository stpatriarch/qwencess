# Generate a documents from source docsritngs

## installing phinx

`pip install sphinx myst-parser sphinx-autodoc-typehints`

## Makeing Sphinx directives

### in project docs directiory do

`sphinx-quickstart`

* Question one `y`
* Question two `developer name`
* Question three `project version`

### in docs direcory do

`mv docsring_gen/conf.py source/conf.py`

**_In source conf.py you need only change this section._**

```py

project = 'Name'
copyright = '2026, stpatriarch'
author = 'stpatriarch'
release = '0.0.1a20260101'

```

## Generates a rst files

### in project root direcory do

`sphinx-apidoc -o docs/source src/project_name`

### Than generate a html, epub docs with

`make html` or `make epub` ect.. for exemple.

For all make commands `make help`

**Now all maked docs you can find in docs/build directory**
