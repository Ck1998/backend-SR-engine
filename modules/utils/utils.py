import magic


def determine_mime_type(content):
    return magic.from_buffer(content, mime=True)
