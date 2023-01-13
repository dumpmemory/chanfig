from json import JSONEncoder
from typing import Any

from yaml import SafeDumper, SafeLoader

from .variable import Variable


class JsonEncoder(JSONEncoder):
    """
    JSON encoder for Config.
    """

    def default(self, o: Any) -> Any:
        if isinstance(o, Variable):
            return o.value
        if hasattr(o, "__json__"):
            return o.__json__()
        return super().default(o)


class YamlDumper(SafeDumper):
    """
    YAML Dumper for Config.
    """

    def increase_indent(self, flow: bool = False, indentless: bool = False):  # pylint: disable=W0235
        return super().increase_indent(flow, indentless)


class YamlLoader(SafeLoader):  # pylint: disable=R0901
    """
    YAML Loader for Config.
    """


class FileError(ValueError):
    """
    Error for file operations.
    """
