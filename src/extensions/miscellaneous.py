# -*- coding: utf-8 -*-
#from hyde.plugin import Plugin

import os
from hyde.plugin import Plugin
from jinja2 import contextfunction


@contextfunction
def listimagedir(context, path):
    """
    Returns a list of all files in the given partial imagepath.
    """
    list = os.listdir('content/media/images/'+path)
    return [context['site'].media_url('images/'+path+i) for i in list]

class Miscellaneous(Plugin):
    def template_loaded(self, template):
            template.env.globals['listimagedir'] = listimagedir
