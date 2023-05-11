import capturecli

command = ['python', '-c', "import sys; print('to stdout'); print('to stderr', file=sys.stderr)"]
command_exit3 = ['python', '-c', "import sys; print('to stdout'); print('to stderr', file=sys.stderr); exit(3)"]

def test_separated_bytes():
    exit_code, out, err = capturecli.separated_bytes(command)
    assert exit_code == 0
    assert out ==  b'to stdout\n'
    assert err ==  b'to stderr\n'

def test_merged_bytes():
    exit_code, out_err = capturecli.merged_bytes(command)
    assert exit_code == 0
    assert out_err ==  b'to stderr\nto stdout\n'

def test_separated():
    exit_code, out, err = capturecli.separated(command)
    assert exit_code == 0
    assert out ==  'to stdout\n'
    assert err ==  'to stderr\n'

def test_merged():
    exit_code, out_err = capturecli.merged(command)
    assert exit_code == 0
    assert out_err ==  'to stderr\nto stdout\n'

def test_separated_exit_code():
    exit_code, out, err = capturecli.separated(command_exit3)
    assert exit_code == 3
    assert out ==  'to stdout\n'
    assert err ==  'to stderr\n'

def test_merged_exit_code():
    exit_code, out_err = capturecli.merged(command_exit3)
    assert exit_code == 3
    assert out_err ==  'to stderr\nto stdout\n'


