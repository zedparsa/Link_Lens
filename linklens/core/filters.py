from typing import Tuple

DEFAULT_EXTENSIONS = ('.mkv', '.mp4', '.zip', '.rar', '.iso', '.exe')

def is_downloadable(url: str, extensions: Tuple[str, ...] = DEFAULT_EXTENSIONS) -> bool:
    """Return True if the URL ends with one of the given extensions."""
    return url.lower().endswith(extensions)
