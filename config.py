from pathlib import Path
import pytomlpp
import string


# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
# 0-9: 0x30-0x39
code_start_number = 0x30
# A-Z: 0x41-0x5A
code_start_alphabet = 0x41


with open(Path(__file__, '..', 'config.toml').resolve(), encoding='utf-8') as f:
    config = pytomlpp.load(f)


for k, v in config['fishing']['key_binding'].items():
    v = str(v).upper()

    if len(v) == 1:
        if v in string.digits:
            config['fishing']['key_binding'][k] = code_start_number + int(v)
            continue
        elif v in string.ascii_uppercase:
            config['fishing']['key_binding'][k] = code_start_alphabet + string.ascii_uppercase.index(v)
            continue

    raise ValueError('Unexpected key binding: %s' % k)
