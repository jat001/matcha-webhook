from pathlib import Path
import pytomlpp


with open(Path(__file__, '..', 'config.toml').resolve(), encoding='utf-8') as f:
    config = pytomlpp.load(f)
