import os
import re
import warnings
from importlib import import_module


class ConfigModule:
    base_runtime = "app.conf.base"
    runtime_pattern = re.compile("^(app.conf)\.S+")

    def __init__(self) -> None:
        self.runtime = os.getenv("FASTAPI_MODULE_RUNTIME", self.base_runtime)
        self.module = None

    def __repr__(self) -> str:
        if self.module is None:
            return "<ConfigModule [Unevaluated]>"

        return f"<ConfigModule {self.runtime}>"

    def setup(self):
        if not self.runtime_pattern.match(self.runtime):
            warnings.warn(
                f"{self.runtime} is issue FASTAPI_MODULE_RUNTIME value, setdefault: {self.base_runtime}",
                stacklevel=2,
            )
            self.runtime = os.environ["FASTAPI_MODULE_RUNTIME"] = self.base_runtime

        try:
            module = import_module(self.runtime)

        except AttributeError as exc:
            raise ImportError(f"ConfigModule {self.runtime!r} import error") from exc

        self.module = module

    def __getattr__(self, attr: str):
        """Return the value of a setting and cache it in self.__dict__."""

        if self.module is None:
            self.setup()

        val = getattr(self.module, attr)
        self.__dict__[attr] = val
        return val


settings = ConfigModule()
