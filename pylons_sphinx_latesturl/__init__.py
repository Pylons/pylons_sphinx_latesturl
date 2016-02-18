
def add_latesturl(app, pagename, templatename, context, doctree):
    config = app.env.config
    base = config.pylons_sphinx_latesturl_base
    if base is not None:
        overrides = getattr(config,
                            'pylons_sphinx_latesturl_pagename_overrides', {})
        pagename = overrides.get(pagename, pagename)
        context['latest_url'] = (
            base + pagename + context.get('file_suffix', '.html'))

def setup(app):
    app.add_config_value('pylons_sphinx_latesturl_base', None, 'rebuild')
    app.add_config_value('pylons_sphinx_latesturl_pagename_overrides',
                         None, 'rebuild')

    app.connect('html-page-context', add_latesturl)
