import os
import logging

_loggingLevels = {
    "INFO": logging.INFO, "DEBUG": logging.DEBUG,
    "CRITICAL": logging.CRITICAL, "ERROR": logging.ERROR,
}

server = {
    "appname": os.getenv('APPNAME', 'svc_smart_cam'),
    "logginglevel": _loggingLevels[os.getenv('LOGGING', 'CRITICAL').upper()],
    "hostname": os.getenv('HOSTNAME', 'localhost'),
    "port": int(os.getenv('PORT', 5000)),
    "namespace": os.getenv('NAMESPACE', "/cv"),
}
