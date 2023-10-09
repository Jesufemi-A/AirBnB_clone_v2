#!/usr/bin/python3
<<<<<<< HEAD
"""function to  generate aa .tgz archive
"""
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ function to generate a a .tgz archive file steming from
    project web_static folder of your AirBnB Clone repo
    """

    local("mkdir -p versions")
    dformat = "%Y%m%d%H%M%S"
    archive_path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), dformat))
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path
=======
"""
This module provides a function to create a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    now = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")

    archived = local("tar -cvzf {} web_static".format(archive_path))

    if archived.return_code != 0:
        return None
    else:
        return archive_path
>>>>>>> c6af4e57b31bb2a256d83b6c36a7b9dc90764ea2
