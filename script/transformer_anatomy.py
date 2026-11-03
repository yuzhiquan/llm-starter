from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "transformer_anatomy.py"), run_name="__main__")
