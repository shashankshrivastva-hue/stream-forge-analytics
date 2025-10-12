"""Columnar analytics store with p50, p95, p99 calculations."""
import numpy as np
from typing import List, Dict, Any

class StreamMetricsStore:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def save_window(self, window_summary: Dict[str, Any]):
        self.history.append(window_summary)

    def calculate_percentiles(self, raw_values: List[float]) -> Dict[str, float]:
        if not raw_values:
            return {"p50": 0.0, "p95": 0.0, "p99": 0.0}
        arr = np.array(raw_values)
        return {
            "p50": round(float(np.percentile(arr, 50)), 2),
            "p95": round(float(np.percentile(arr, 95)), 2),
            "p99": round(float(np.percentile(arr, 99)), 2)
        }
