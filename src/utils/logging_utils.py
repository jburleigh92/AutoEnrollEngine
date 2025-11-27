import sys
import traceback


def info(message: str) -> None:
    """
    Write a standard informational log message.
    """
    sys.stdout.write(message + "\n")
    sys.stdout.flush()


def error(message: str, exc: Exception = None) -> None:
    """
    Write an error log message, optionally including a traceback.
    """
    sys.stderr.write("ERROR: " + message + "\n")

    if exc:
        traceback.print_exc(file=sys.stderr)

    sys.stderr.flush()
