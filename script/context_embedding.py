from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "context_embedding.py"), run_name="__main__")
