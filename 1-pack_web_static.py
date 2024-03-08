#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo,
    using the function do_pack

    Usage:
        fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
from fabric.decorators import runs_once
from datetime import datetime


@runs_once
def do_pack():
    """
        function that archives .tgz web_static content.
    """
    local('mkdir -p versions')
    time = datetime.now()
    current_time = time.strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(current_time)
    result = local(
        'sudo tar -czvf {} web_static'
        .format(path)
    )
    return None if result.failed else path
