from eventlet.support import six

from eventlet._basegreenio import _GLOBAL_DEFAULT_TIMEOUT  # noqa
from eventlet._basegreenio import *  # noqa

if six.PY2:
    from eventlet._py2greenio import _fileobject  # noqa
    from eventlet._py2greenio import *  # noqa
else:
    from eventlet._py3greenio import _fileobject  # noqa
    from eventlet._py3greenio import *  # noqa


__all__ = ['GreenSocket', 'GreenPipe', 'shutdown_safe']
