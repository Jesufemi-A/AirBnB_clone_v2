#!/usr/bin/python3
""" script for fabric module for deployment
"""
from fabric.api import local, env, put, run, cd, lcd
from datetime import datetime
from os import path, listdir
from fabric.decorators import runs_once


env.hosts = ['54.237.65.38', '54.237.210.238']

# Set the username
env.user = "ubuntu"

# Set private key path
env.key_filename = "~/.ssh/id_rsa"


@runs_once
def do_pack():
    """ generates a .tgz archive file steming from
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


def do_deploy(archive_path):
    """function to distribute web server archieve """

    try:
        if not path.exists(archive_path):
            return False

        dir_path = "/data/web_static/releases/"
        filename = path.basename(archive_path)
        file_no_ext, ext = path.splitext(filename)
        put(archive_path, "/tmp/{}".format(filename))
        run("rm -rf {}{}".format(dir_path, file_no_ext))
        run("mkdir -p {}{}".format(dir_path, file_no_ext))
        run("tar -xzf /tmp/{} -C {}{}".format(filename, dir_path, file_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dir_path, file_no_ext))
        run("rm -rf {}{}/web_static".format(dir_path, file_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(
            dir_path, file_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """function to distribute web server archieve"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """function to delete outdated web server archive"""
    nbr = 2 if int(number) == 0 else int(number) + 1

    with lcd("versions"):
        local("ls -dt * | tail -n +{} | sudo xargs rm -f".format(nbr))
    with cd("/data/web_static/releases"):
        run("ls -dt * | tail -n +{} | sudo xargs rm -rf".format(nbr))
