# -*- coding: utf-8 -*-
#from hyde.plugin import Plugin

import os
from hyde.plugin import Plugin
from jinja2 import contextfunction


@contextfunction
def listdir(context, path):
    """
    Returns a list of all files in the given partial path.
    """
    #return  os.listdir(context['site'].content_url(path))
    #return  os.listdir(context['site'].media_url(path))
    list = os.listdir(path)
    #return [os.path.join(root,i) for i in list]
    return [context['site'].media_url('images/'+i) for i in list]
    #return os.listdir('.')
    #return list
    #return path

class Miscellaneous(Plugin):

    def template_loaded(self, template):
            template.env.globals['listdir'] = listdir
