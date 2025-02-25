class InvalidTokenError(Exception):

    def __init__(self, token, msg="Invalid token placement"):
        self.token = token
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.token}: {self.msg}'

class InvalidDesignTileError(Exception):

    def __init__(self, token, msg="Invalid design tile placement"):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.token}: {self.msg}'
    
# class UnrecognizedObject(Exception):
    
#     def __init__(self, msg="Object not recognized"):
#         self.msg = msg
#         super().__init__(self.msg)
    
# class UnrecognizedTileError(UnrecognizedObject):

#     def __init__(self, msg="Tile not recognized"):
#         self.msg = msg
#         super().__init__(self.msg)
    
# class UnrecognizedTokenError(UnrecognizedObject):

#     def __init__(self, msg="Token not recognized"):
#         self.msg = msg
#         super().__init__(self.msg)
