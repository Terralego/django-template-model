from base64 import b64decode, b64encode
from enum import Enum


class FmtMimeMapping(Enum):
    docx = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    odt = 'application/vnd.oasis.opendocument.text'
    html = 'text/html'


def from_bytes_to_str(b_obj, fmt):
    if fmt == 'html':
        return b_obj.decode()
    elif fmt == 'odt' or fmt == 'docx':
        return b64encode(b_obj).decode()
    else:
        return None


def from_str_to_bytes(str_obj, fmt):
    if fmt == 'odt' or fmt == 'docx':
        return b64decode(str_obj.encode())
    elif fmt == 'html':
        return str_obj.encode()
    else:
        return None
