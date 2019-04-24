

class VerpyError(Exception):
    pass

class VerpyWarning(Warning):
    pass

class InternalFatal(VerpyError):
    pass

class ParserContextError(VerpyError):
    pass

class VerpySyntaxError(VerpyError):
    pass

class RegexReplaceError(VerpyError):
    pass

class VerpyUserError(VerpyError):
    pass

class VerpyElabError(VerpyError):
    pass

class VerpyLibraryError(VerpyError):
    pass

class PatternNotFoundWarning(VerpyWarning):
    pass

