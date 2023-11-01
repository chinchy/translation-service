from math import ceil
from typing import Any

from fastapi.responses import ORJSONResponse
from starlette import status


def single_item(data: dict[str, Any]) -> ORJSONResponse:
    return ORJSONResponse(status_code=status.HTTP_200_OK, content={"data": {"item": data}})


def paginated_items(
    data: list[dict[str, Any]],
    *,
    page: int,
    per_page: int,
    total_item_count: int,
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "items": data,
                "total_item_count": total_item_count,
                "page": page,
                "per_page": per_page,
                "page_count": ceil(total_item_count / per_page),
            }
        },
    )
