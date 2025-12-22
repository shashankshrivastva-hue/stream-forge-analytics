# 🌊 StreamForge Analytics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

High-throughput, real-time event streaming and analytical windowing engine with live WebSocket pub/sub.

---

## 🏛️ Pipeline Flow

```mermaid
flowchart LR
    IoT[Event Producer / IoT] -->|JSON Stream| WS[WebSocket Ingestion]
    WS --> Agg[Tumbling Window Aggregator]
    Agg --> Store[Columnar Metrics Store]
    Store --> Calc[P50 / P95 / P99 Analytics]
    Calc --> Broadcast[Live WebSocket Broadcast]
    Broadcast --> UI[Real-Time Analytics Dashboard]
```

## 🚀 Features

- **Tumbling & Sliding Windowing**: Micro-batch aggregation with configurable time horizons.
- **Statistical Rollups**: Computes p50, p95, p99 latency distributions on the fly.
- **AsyncIO Concurrency**: Broadcasts analytics to thousands of connected clients with low memory overhead.

## 🛠️ Usage

```bash
pip install -r requirements.txt
uvicorn src.api.server:app --port 8000
```

## 📜 License
MIT License. Built by [Shashank Shrivastva](https://github.com/shashankshrivastva-hue).
