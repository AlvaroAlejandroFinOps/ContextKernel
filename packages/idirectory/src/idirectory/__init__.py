"""iDirectory L0 topological control plane."""
try:
    from core import fwengine, context_runtime
except ImportError:
    try:
        from ..core import fwengine, context_runtime
    except ImportError:
        fwengine = None
        context_runtime = None

__version__ = "6.1.0"
__all__ = ["fwengine", "context_runtime"]
