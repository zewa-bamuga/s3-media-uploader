from collections.abc import Callable
from fastapi import Query

from a8t_tools.db import pagination, sorting


def get_skip_limit_pagination_dep(
        schema: type[pagination.SchemaType],
) -> Callable[[int, int], pagination.PaginationCallable[pagination.SchemaType]]:
    def get_skip_limit_pagination(
            skip: int = Query(0), limit: int = Query(100)
    ) -> pagination.PaginationCallable[pagination.SchemaType]:
        return pagination.skip_limit_pagination_factory(schema, skip, limit)

    return get_skip_limit_pagination


def get_sort_order_sorting_dep(
        sort_field_type: type[sorting.SortFieldType],
        default_field: sorting.SortFieldType | None = None,
        default_order: sorting.SortOrders = sorting.SortOrders.asc,
) -> Callable[[sorting.SortFieldType | None, sorting.SortOrders], sorting.SortingData[sorting.SortFieldType],]:
    def get_sort_order_sorting(
            sort: sort_field_type | None = Query(default_field),  # type: ignore [valid-type]
            order: sorting.SortOrders = Query(default_order),
    ) -> sorting.SortingData[sorting.SortFieldType]:
        return sorting.SortingData[sort_field_type](field=sort, order=order)  # type: ignore [valid-type]

    return get_sort_order_sorting
