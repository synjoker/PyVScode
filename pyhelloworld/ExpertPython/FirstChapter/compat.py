import sys
if sys.version_info < (3, 0, 0):
    import urlparse 
    def is_string(s):
        return isinstance(s, basestring)
else:
    from urllib import parse as urlparse
    def is_string(s):
        return isinstance(s, str)