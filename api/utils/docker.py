import os


def is_running_in_docker():
    if os.path.exists("/.dockerenv"):
        return True

    try:
        with open("/proc/1/cgroup", "r") as f:
            if "docker" in f.read() or "/docker/" in f.read():
                return True
    except FileNotFoundError:
        pass

    return False
