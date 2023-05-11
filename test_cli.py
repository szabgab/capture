import capturecli

def test_cli():
    command = ['python', '-c', "import sys; print('to stdout'); print('to stderr', file=sys.stderr)"]

    exit_code, out, err = capturecli.separated_bytes(command)
    assert exit_code == 0
    assert out ==  b'to stdout\n'
    assert err ==  b'to stderr\n'

    exit_code, out_err = capturecli.merged_bytes(command)
    assert exit_code == 0
    assert out_err ==  b'to stderr\nto stdout\n'

    exit_code, out, err = capturecli.separated(command)
    assert exit_code == 0
    assert out ==  'to stdout\n'
    assert err ==  'to stderr\n'

    exit_code, out_err = capturecli.merged(command)
    assert exit_code == 0
    assert out_err ==  'to stderr\nto stdout\n'

def test_cli_exit_code():
    command = ['python', '-c', "import sys; print('to stdout'); print('to stderr', file=sys.stderr); exit(3)"]

    exit_code, out, err = capturecli.separated(command)
    assert exit_code == 3
    assert out ==  'to stdout\n'
    assert err ==  'to stderr\n'

    exit_code, out_err = capturecli.merged(command)
    assert exit_code == 3
    assert out_err ==  'to stderr\nto stdout\n'


