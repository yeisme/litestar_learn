from litestar import Litestar, Response, get


def after_request_app(response: Response) -> Response:
    # 应用层after_request钩子
    return Response(content=b"app after request")


def after_request_handler(response: Response) -> Response:
    # 路由处理函数层after_request钩子
    return Response(content=b"handler after request")


@get("/")
async def handler() -> str:
    # 没有设置钩子，会使用应用层的after_request
    return "hello, world"


@get("/override", after_request=after_request_handler)
async def handler_with_override() -> str:
    # 设置了handler_with_override自己的after_request钩子
    return "hello, world"


app = Litestar(
    route_handlers=[handler, handler_with_override],
    after_request=after_request_app,  # 应用层设置after_request
)
