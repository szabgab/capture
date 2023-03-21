import subprocess

def separated(command):
    '''
    >>> exit_code, out, err = separated(['ls', '-l'])
    '''
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )  # This starts runing the external process
    out, err = proc.communicate()
    exit_code = proc.returncode
    return exit_code, out, err


def merged(command):
    '''
    >>> exit_code, out_err = merged(['ls', '-l'])
    '''
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
    )  # This starts runing the external process
    out, err = proc.communicate()

    exit_code = proc.returncode
    return exit_code, out

