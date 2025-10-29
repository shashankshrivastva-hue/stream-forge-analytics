"""FastAPI streaming server with real-time WebSocket broadcast."""
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from ..engine.window_aggregator import TumblingWindowAggregator

app = FastAPI(title="StreamForge Real-Time Analytics Engine")
aggregator = TumblingWindowAggregator(window_seconds=5)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                pass

manager = ConnectionManager()

@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            window_summary = aggregator.ingest(data)
            if window_summary:
                await manager.broadcast(window_summary)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
