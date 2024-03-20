#!/usr/bin/python3
"""script that distributes an archive to your web servers """
import os
from datetime import datetime
from fabric.api import local, put, run, env

env.hosts = ['54.237.102.87', '54.210.57.49']
env.user = "ubuntu"


def do_pack():
    """Archives the contents of the static files."""
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    timestamp = datetime.now().strftime(time_format)
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    try:
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        archize_size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes"
              .format(archive_path, archize_size))
    except Exception:
        archive_path = None
    return archive_path


def do_deploy(archive_path):
    """ Distributes an archive to your web servers
    Args:
        archive_path (str): The path to the archive file to be deployed.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """

    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    is_success = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        is_success = True
    except Exception:
        is_success = False
    return is_success


def deploy():
    """Archives and deploys the static fully to servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """script that deletes out-of-date archives"""

    archive_list = os.listdir('versions/')
    archive_list.sort(reverse=True)
    number = int(number)

    if not number:
        number += 1
    if number < len(archive_list):
        archive_list = archive_list[number:]
    else:
        archive_list = []
    for archive in archive_list:
        os.unlink('versions/{}'.format(archive))

    cleanup_cmd = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(number + 1)
    ]
    run(''.join(cleanup_cmd))
