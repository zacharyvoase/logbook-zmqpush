import zmq
import logbook.queues


class ZeroMQPushHandler(logbook.queues.ZeroMQHandler):

    """
    A handler that pushes JSON log records over a ZMQ socket.

    Specifically, this handler opens a ``zmq.PUSH`` socket and connects to a
    ``zmq.PULL`` socket at the specified address. You can use
    :class:`ZeroMQPullSubscriber` to receive the log record.

    Example:

        >>> import logbook
        >>> handler = ZeroMQPushHandler('tcp://127.0.0.1:5501')
        >>> with handler.applicationbound():
        ...     logbook.debug("Something happened")
    """

    def __init__(self, addr=None, level=logbook.NOTSET, filter=None,
                 bubble=False, context=None):
        logbook.Handler.__init__(self, level, filter, bubble)

        self.context = context or zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        if addr is not None:
            self.socket.connect(addr)


class ZeroMQPullSubscriber(logbook.queues.ZeroMQSubscriber):

    """
    A subscriber which listens on a PULL socket for log records.

    This subscriber opens a ``zmq.PULL`` socket and binds to the specified
    address. You should probably use this in conjunction with
    :class:`ZeroMQPushHandler`.

    Example:

        >>> subscriber = ZeroMQPullSubscriber('tcp://*:5501')
        >>> log_record = subscriber.recv()
    """

    def __init__(self, addr=None, context=None):
        self.context = context or zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        if addr is not None:
            self.socket.bind(addr)