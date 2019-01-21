class ApiError(Exception):
    def __init__(self, msg, code, submsg=None, subcode=None, params=None):
        self.message = msg
        self.submsg = submsg
        self.code = code
        self.subcode = subcode
        self.params = params

    def __str__(self):
        return f'{self.message}({self.code})' \
               + (f', {self.submsg}({self.subcode})' if self.submsg else '') \
               + (f', params: {self.params}' if self.params else '')
