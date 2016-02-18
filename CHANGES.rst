``pylons_sphinx_latesturl`` Changelog
=====================================

- When RTD is building json output the ``context`` is missing the
  ``file_suffix`` option but it seems safe to assume ``.html``::

  sphinx-build -T -b json -d _build/doctrees-json -D language=en . _build/json

0.1.1 (2013-09-09)
------------------

- Initial release.
