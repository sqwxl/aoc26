import importlib.util
import sys
import time
from pathlib import Path

input_path = Path("inputs")
solution_path = Path("solutions")


def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec
    assert spec.loader

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def solve(data: Path, ab: str | None = None):
    solver = import_from_path(data.name, solution_path / f"s{data.name}.py")
    text = data.read_text().strip()
    if ab is None or ab == "a":
        t0 = time.perf_counter()
        a = solver.a(text)
        t1 = time.perf_counter()
        print(f"a: {a} ({(t1 - t0) * 1000:.2f}ms)")
    if ab is None or ab == "b":
        t0 = time.perf_counter()
        b = solver.b(text)
        t1 = time.perf_counter()
        print(f"b: {b} ({(t1 - t0) * 1000:.2f}ms)")


def main():
    if len(sys.argv) > 1:
        path = input_path / sys.argv[1]
        ab = sys.argv[2] if len(sys.argv) > 2 else None
        solve(path, ab)
        return

    for i in input_path.iterdir():
        solve(i)


if __name__ == "__main__":
    main()
