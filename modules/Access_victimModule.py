import os

def access(REMOTE_HOST, REMOTE_PORT):
    command = "wsl stty raw -echo; (stty size; cat) | wsl nc -lvnp {} -s {}".format(REMOTE_PORT, REMOTE_HOST)
    os.system(command)