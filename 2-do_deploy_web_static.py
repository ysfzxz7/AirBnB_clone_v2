#!/usr/bin/python3
"""
    Script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo,
    using the function do_pack, and another function that
    distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.26.231.82', '100.26.171.172']
env.user = 'ubuntu'


@runs_once
def do_pack():
    """
        Function that archives .tgz web_static content.
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


def do_deploy(archive_path):
    """
        Function that distributes an archive to your web servers
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
