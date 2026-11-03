from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent.parent / "tokenizer_demo.py"), run_name="__main__")
