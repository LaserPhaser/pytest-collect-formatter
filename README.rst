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


Example of usage
----------------
    $ pytest tests --collect-output-file my_tests_structure.xml --collect-format xml

And you will get the my_tests_structure.xml

Exmpales of formats
-------------------

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


