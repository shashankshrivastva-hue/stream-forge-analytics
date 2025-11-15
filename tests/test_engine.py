from src.engine.metrics_store import StreamMetricsStore

def test_percentile_calculations():
    store = StreamMetricsStore()
    values = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    p = store.calculate_percentiles(values)
    assert p["p50"] == 55.0
    assert p["p95"] > 90.0
    assert p["p99"] > 95.0
