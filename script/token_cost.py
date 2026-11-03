from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "token_cost.py"), run_name="__main__")
