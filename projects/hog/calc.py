import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

