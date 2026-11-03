from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "train_tiny.py"), run_name="__main__")
