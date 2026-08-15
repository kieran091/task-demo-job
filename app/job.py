#!/usr/bin/env python3
"""Small deterministic task runner for Worklane task/v1."""

import os
import sys
from datetime import datetime, timezone


def main() -> int:
    raw_count = os.getenv("TASK_COUNT", "3")
    try:
        count = int(raw_count)
    except ValueError:
        print("TASK_COUNT must be an integer between 1 and 100", file=sys.stderr)
        return 2
    if not 1 <= count <= 100:
        print("TASK_COUNT must be an integer between 1 and 100", file=sys.stderr)
        return 2

    for index in range(1, count + 1):
        timestamp = datetime.now(timezone.utc).isoformat()
        print(f"processed task {index}/{count} at {timestamp}", flush=True)
    print(f"task-demo-job completed: {count} tasks", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
