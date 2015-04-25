Pyslate syntax reference
========================

Decorators
----------

.. _Available_Decorators:

Available decorators
^^^^^^^^^^^^^^^^^^^^

By default Pyslate provides the following decorators in the default scope:

 - ``capitalize`` - make the first character have upper case and the rest lower case
 - ``upper`` - convert to uppercase
 - ``lower`` - convert to lowercase

For English an additional decorator is available:

 - ``article`` - add *a* or *an* article to a word. *An* is added if the first letter of the word is a vowel, *a* otherwise.
