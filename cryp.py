#Encrypted with Crypton
#Created by OVERDOSIS
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))