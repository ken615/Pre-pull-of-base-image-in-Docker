import subprocess

def main():
    cmd = "python -V"
    process = (subprocess.Popen(cmd, 
                                stdout=subprocess.PIPE,
                                shell=True).communicate()[0]).decode('utf-8')
    version = (process.split(" "))[1]
    version = version.rstrip("\r\n")
    return version