__all__ = ['properties']


try:
    from jaraco.classes import properties  # pragma: no-cover
except ImportError:
    from . import _properties_compat as properties  # type: ignore[no-redef] # pragma: no-cover
