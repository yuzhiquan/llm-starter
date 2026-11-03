from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "scaling_law.py"), run_name="__main__")
