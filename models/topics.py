
# {
#     'topics': ['joy', 'intro', 'kindness']
# }

class Topics:
    _topic_list = [
        'intro', 'kindness', 'discovery', 'joy', 'shared resource',
        'shadow challenge', 'heroic', 'action'
    ]

    @classmethod
    def isValid(cls, string):
        if string in cls._topic_list:
            return True
        return False
