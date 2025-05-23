"""Dummy Domain file to test domain loading with config
for further testing, like docker file generation
"""

from protean.domain import Domain

domain = Domain(name="SQLite-Domain")


domain.config["databases"] = {
    "default": {
        "provider": "sqlite",
        "database_uri": "sqlite:///:memory:",
    }
}
