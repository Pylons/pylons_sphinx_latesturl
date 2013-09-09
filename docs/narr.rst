:mod:`pylons_sphinx_latesturl`
===============================

This package is a :mod:`Sphinx` extension:  it adds a function to the 
Sphinx template namespace which can be used to compute the "latest" URL
for a versioned document.

Versioned Documentation
-----------------------
    
For instance, suppose you have released both
version ``1.0`` and ``1.1`` of the ``frobnaz`` project, and publshed
documentation for them as:

  http://frobnaz.readthedocs.org/en/1.0/

and:

  http://frobnaz.readthedocs.org/en/latest/

On each page of the ``1.0`` version of the docs, you would like to link to
the corresponding page in the latest version of the docs, e.g.
on the ``tutorials/spamqux`` page:

.. code-block:: html

   <p> These docs are for version <code>1.0</code> of this package.  For
   the latest version, see:
   <a href="http://frobnaz.readthedocs.org/en/latest/tutorials/spamqux">
   this page</a></p>

Rather than maintaining those links on every page of the ``1.0``
documentation, it would be useful to compute the URL in your theme.
E.g., you could add something like the following to the
``layout.html`` of your Sphinx theme:

.. code-block:: jinja

   <p> These docs are for version <code>1.0</code> of this package.  For
   the latest version, see:
   <a href="http://frobnaz.readthedocs.org/en/latest/{{ pagename }}{ file_suffix }}">this page</a>.</p>
   
So for, this approach doesn't require any extension:  it works fine in vanilla
Sphinx.

Overriding ``pagename``
-----------------------

The approach above assumes that the latest version of the docs has the
identical page structure as the earlier, versioned docs (at least, that
for each page in the versioned docs, there is a page in the latest version
with the same name).

If you have reorganized the documentation over time, the correspondence may
not be an exact fit.  For instance, the ``tutorials/spamqux`` page referenced
above may be called ``tutorial/spam-and-qux`` in the latest docs.  Enter
this package, which provides a way to compute a new ``pagename`` using
configured values.

To configure, add this extension to the :file:`conf.py` of your Sphinx:

.. code-block:: python

    extensions = [
        # ...
        'pylons_sphinx_latesturl',
    ]


and then define two configuration options in that same file:

.. code-block:: python

   pylons_sphinx_latesturl_base = (
       'http://frobnaz.readthedocs.org/en/latest/')

   pylons_sphinx_latesturl_pagename_overrides = {
       'tutorials/spamqux`: 'tutorial/spam-and-qux',
   }

You will then need to use the ``latest_url`` value (as computed by
the extension) in its ``layout.html`` template:

.. code-block:: jinja

   <p> These docs are for version <code>1.0</code> of this package.  For
   the latest version, see: <a href="{{ latest_url }}">this page</a>.</p>

On pages for which no override is defined, the ``latest_url`` value will
be computed as above, by concatenating the value defined in
``theme_options['latest_url']`` with ``pagename`` and ``file_suffix``.
For pages whose ``pagename`` **does** have an override, that value will
be substituted for ``pagename``.
