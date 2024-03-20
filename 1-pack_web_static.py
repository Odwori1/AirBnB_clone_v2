#!/usr/bin/python3
"""script that gen .tgz archive from contents of web_static folder """
import os
from datetime import datetime
from fabric.api import local


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
        print("web_static packed: {} -> {} Bytes".format(
            archive_path, archize_size))
    except Exception:
        archive_path = None
    return archive_path
