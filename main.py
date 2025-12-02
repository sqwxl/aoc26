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


def solve(data: Path):
    solver = import_from_path(data.name, solution_path / f"s{data.name}.py")
    text = data.read_text().strip()
    t0 = time.perf_counter()
    a = solver.a(text)
    t1 = time.perf_counter()
    print(f"a: {a} ({(t1 - t0) * 1000:.2f}ms)")
    b = solver.b(text)
    t2 = time.perf_counter()
    print(f"b: {b} ({(t2 - t1) * 1000:.2f}ms)")


def main():
    if len(sys.argv) > 1:
        solve(input_path / sys.argv[1])
        return

    for i in input_path.iterdir():
        solve(i)


if __name__ == "__main__":
    main()
