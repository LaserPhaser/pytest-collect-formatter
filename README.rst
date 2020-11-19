========================
pytest-collect-formatter
========================





Pytest plugin for formatting output of the collected tests.


* Free software: MIT license


Requirements
------------

* pyyaml
* dicttoxml



Installation
------------

You can install "pytest-collect-formatter" via `pip`_::

    $ pip install pytest-collect-formatter


Usage
-----
* Use this plugin by running pytest normally and use the following options to customize collection format,
  it's better to use with `--collect-only` option


>>> collect-formatter:
  --collect-output-file=COLLECT_OUTPUT_FILE
                        Saves collected test items to the file
  --collect-format=COLLECT_FORMAT
                        Saves collected test items specified format [xml, yaml, json]
  --collect-type=COLLECT_TYPE
                        Format output results in classic pytest view or in 'path' view [classic, path], default classic



Example of usage
----------------
    $ pytest tests --collect-output-file my_tests_structure.xml --collect-format xml

And you will get the my_tests_structure.xml

Exmpales of formats
-------------------
PATH
____

JSON

.. code-block::

    [
        {
            "type": "path",
            "title": "examples",
            "children": [
                {
                    "type": "path",
                    "title": "tests",
                    "children": [
                        {
                            "type": "path",
                            "title": "test_formatter",
                            "children": [
                                {
                                    "type": "path",
                                    "title": "test_fromatter_v1.py",
                                    "children": [
                                        {
                                            "type": "pytest_unit",
                                            "title": "TestFormatter",
                                            "children": [
                                                {
                                                    "type": "pytest_unit",
                                                    "title": "test_inside_class",
                                                    "children": []
                                                },
                                                {
    ...



YAML

.. code-block::

    - children:
      - children:
        - children:
          - children:
            - children:
              - children: []
                title: test_inside_class
                type: pytest_unit
              - children: []
                title: test_inside_class_parametrize[1]
                type: pytest_unit
              - children: []
                title: test_inside_class_parametrize[2]
                type: pytest_unit
              - children: []
                title: test_inside_class_parametrize[3]
   ...

XML

.. code-block::

    <?xml version="1.0" ?>
    <root>
        <item>
            <type>path</type>
            <title>examples</title>
            <children>
                <item>
                    <type>path</type>
                    <title>tests</title>
                    <children>
                        <item>
                            <type>path</type>
                            <title>test_formatter</title>
                            <children>
                                <item>
                                    <type>path</type>
                                    <title>test_fromatter_v1.py</title>
                                    <children>
                                        <item>
                                            <type>pytest_unit</type>
                                            <title>TestFormatter</title>
                                            <children>
                                                <item>
                                                    <type>pytest_unit</type>
                                                    <title>test_inside_class</title>
                                                    <children/>
                                                </item>
    ...


CLASSIC
_______
JSON

.. code-block::

   [
    {
        "type": "Package",
        "value": "test_formatter",
        "children": [
            {
                "type": "Module",
                "value": "test_fromatter_v1.py",
                "children": [
                    {
                        "type": "Class",
                        "value": "TestFormatter",
                        "children": [
                            {
                                "type": "Function",
                                "value": "test_inside_class"
                            }
    ....

YAML

.. code-block::

    - children:
      - children:
        - children:
          - type: Function
            value: test_inside_class
          - type: Function
            value: test_inside_class_parametrize[1]
          - type: Function
            value: test_inside_class_parametrize[2]
          - type: Function
            value: test_inside_class_parametrize[3]
          - type: Function
            value: test_inside_class_parametrize[4]
          type: Class
          value: TestFormatter
        - type: Function
          value: test_outside_of_class
        type: Module
        value: test_fromatter_v1.py
      type: Package
      value: test_formatter
    ....


XML

.. code-block::

    <?xml version="1.0" ?>
    <root>
        <item>
            <type>Package</type>
            <value>test_formatter</value>
            <children>
                <item>
                    <type>Module</type>
                    <value>test_fromatter_v1.py</value>
                    <children>
                        <item>
                            <type>Class</type>
                            <value>TestFormatter</value>
                            <children>
                                <item>
                                    <type>Function</type>
                                    <value>test_inside_class</value>
                                </item>
                                <item>
                                    <type>Function</type>
                                    <value>test_inside_class_parametrize[1]</value>
                                </item>
                                <item>
                                    <type>Function</type>
                                    <value>test_inside_class_parametrize[2]</value>
                                </item>
                                <item>
                                    <type>Function</type>
                                    <value>test_inside_class_parametrize[3]</value>
                                </item>
                                <item>
                                    <type>Function</type>
                                    <value>test_inside_class_parametrize[4]</value>
                                </item>
                            </children>
                        </item>
                        <item>
                            <type>Function</type>
                            <value>test_outside_of_class</value>
                        </item>
                    </children>
                </item>
            </children>
    ....

More examples could be found in examples folder as well as tests structure



Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


Credits
-------



.. _`file an issue`: https://github.com/pytest-dev/pytest-slack/issues
.. _`pip`: https://pypi.python.org/pypi/pip/


