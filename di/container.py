from dishka import AsyncContainer, Provider, make_async_container

from .database.connection import DBProvider
from .database.repos import ReposProvider
from .nats.connection import NatsProvider


def make_container(extra_providers: list[Provider] | None = None) -> AsyncContainer:
    if not extra_providers:
        extra_providers = []

    return make_async_container(
        DBProvider(),
        NatsProvider(),
        ReposProvider(),
        *extra_providers,
    )
