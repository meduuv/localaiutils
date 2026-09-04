"""Local inference configuration helpers."""

from urllib.parse import urljoin


def endpoint(base_url: str, path: str = "") -> str:
    """Build an endpoint URL while preserving the base host."""
    return urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))


def model_name(config: dict, default: str = "") -> str:
    """Read a model name from common configuration keys."""
    return str(config.get("model") or config.get("model_name") or default)
