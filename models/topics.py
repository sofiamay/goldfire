
# {
#     'topics': ['joy', 'intro', 'kindness']
# }

class Topics:
    _topic_dict = {
        1: 'Intro',
        2: 'Kindness',
        3: 'Discovery',
        4: 'Joy',
        5: 'Shared Sesource',
        6: 'Shadow challenge',
        7: 'Heroic',
        8: 'Action',
    }

    @classmethod
    def isValid(cls, string):
        if string in list(cls._topic_dict.values()):
            return True
        return False

    @classmethod
    def pprint(cls):
        return '\n'.join([
            "{0}: {1}".format(key, topic)
            for key, topic in cls._topic_dict.items()
        ])
        # return '\n'.join(list_of_topic_strings)
