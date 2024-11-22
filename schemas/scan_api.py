from pydantic import Field

from schemas.base import BaseSchema


class ScanRequest(BaseSchema):
    targets: list[str]


class ScanResponse(BaseSchema):
    task_id: str


class Vulnerability(BaseSchema):
    title: str | None = None
    description: str | None = None
    severity: str | None = None


class PortSchema(BaseSchema):
    port: int
    type: str | None = None
    protocol: str | None = None
    service: str | None = None
    version: str | None = None
    vulnerabilities: list[Vulnerability] = Field(default_factory=list)


class PortsSchema(BaseSchema):
    open: list[PortSchema]
    closed: list[int]


class IpSchema(BaseSchema):
    ip: str
    ptr: str
    ports: PortsSchema


class ScanTaskResponse(BaseSchema):
    task_id: str
    end: bool
    ips: list[IpSchema]
