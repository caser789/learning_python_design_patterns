class HealthCheck(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not HealthCheck._instance:
            HealthCheck._instance = super(
                HealthCheck, cls).__new__(cls, *args, **kw)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")
