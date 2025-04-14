"""
litestar run
# Or you can run Uvicorn directly:
uvicorn app:app --reload
"""

from litestar.openapi import OpenAPIConfig
from litestar import Litestar, get, Request
from litestar.contrib.opentelemetry import OpenTelemetryConfig, OpenTelemetryPlugin
from litestar.openapi.plugins import ScalarRenderPlugin


# 创建配置实例（默认使用全局 Provider）
open_telemetry_config = OpenTelemetryConfig()


@get("/")
async def index(request: Request) -> str:
    request.logger.info("inside a request")
    return "Hello, world!"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar(
    plugins=[OpenTelemetryPlugin(config=open_telemetry_config)],
    openapi_config=OpenAPIConfig(
        title="litestar_learn",
        version="1.0.0",
        description="A simple Litestar app",
        render_plugins=[ScalarRenderPlugin()],
    ),
    debug=True,
    route_handlers=[index, get_book],
    middleware=[],
)
