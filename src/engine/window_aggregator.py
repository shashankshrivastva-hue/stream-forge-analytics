"""Tumbling and hopping window aggregations for streaming metrics."""
import time
from typing import List, Dict, Any

class TumblingWindowAggregator:
    def __init__(self, window_seconds: int = 10):
        self.window_seconds = window_seconds
        self.current_window_start = int(time.time())
        self.events: List[Dict[str, Any]] = []

    def ingest(self, event: Dict[str, Any]) -> Dict[str, Any] | None:
        now = int(time.time())
        aggregated_result = None

        if now - self.current_window_start >= self.window_seconds:
            aggregated_result = self._flush(self.current_window_start, now)
            self.current_window_start = now
            self.events = []

        self.events.append(event)
        return aggregated_result

    def _flush(self, start_ts: int, end_ts: int) -> Dict[str, Any]:
        count = len(self.events)
        latencies = [e.get("latency_ms", 0.0) for e in self.events]
        avg_latency = sum(latencies) / count if count > 0 else 0.0
        
        return {
            "window_start": start_ts,
            "window_end": end_ts,
            "event_count": count,
            "avg_latency_ms": round(avg_latency, 2),
            "events_per_sec": round(count / max(1, end_ts - start_ts), 2)
        }
