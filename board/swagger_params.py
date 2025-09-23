from drf_yasg import openapi

job_filter_params = [
    openapi.Parameter(
        "location",
        openapi.IN_QUERY,
        description="Filter by location",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "type",
        openapi.IN_QUERY,
        description="Filter by job type",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "industry",
        openapi.IN_QUERY,
        description="Filter by industry",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "salary_min",
        openapi.IN_QUERY,
        description="Filter by min salary",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "salary_max",
        openapi.IN_QUERY,
        description="Filter by max salary",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "search",
        openapi.IN_QUERY,
        description="Search jobs",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "ordering",
        openapi.IN_QUERY,
        description="Order by fields",
        type=openapi.TYPE_STRING,
    ),
]
