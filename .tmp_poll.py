import json
import time
from pathlib import Path

path = Path(r"d:\YoloWebAgentStarter\data\runs\training\train_0692d56bd3154b13b498d4bb1f3c15f6\training_summary.json")
deadline = time.time() + 55 * 60
while time.time() < deadline:
    if path.exists():
        try:
            status = json.loads(path.read_text(encoding="utf-8")).get("status")
        except Exception:
            status = None
        if status in ("completed", "failed"):
            print("DONE status=" + str(status))
            raise SystemExit(0)
    time.sleep(30)
print("TIMEOUT")
