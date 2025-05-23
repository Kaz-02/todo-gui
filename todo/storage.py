import json, pathlib

FILE = pathlib.Path("tasks.json")

def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
