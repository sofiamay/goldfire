
# {
#     'topics': ['joy', 'intro', 'kindness']
# }

# class Topics:
#     topic_dict = {
#         1: 'Intro',
#         2: 'Kindness',
#         3: 'Discovery',
#         4: 'Joy',
#         5: 'Shared Sesource',
#         6: 'Shadow challenge',
#         7: 'Heroic',
#         8: 'Action',
#     }

#     @classmethod
#     def isValid(cls, string):
#         if string in list(cls.topic_dict.values()):
#             return True
#         return False

#     @classmethod
#     def pprint(cls):
#         return '\n'.join([
#             "{0}: {1}".format(key, topic)
#             for key, topic in cls.topic_dict.items()
#         ])
#         # return '\n'.join(list_of_topic_strings)

# Private
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


class Topics:
    # Class attribute:
    all_topics = _topic_dict

    def __init__(self, dict):
        self._topic_dict = dict

    def __len__(self):
        return len(self._topic_dict)

    def contains(self, string):
        if string in list(self._topic_dict.values()):
            return True
        return False

    def add(self, string):
        index = len(self._topic_dict) + 1
        self._topic_dict[index] = string

    def remove(self, index):
        self._topic_dict.pop(index)

    def removeByTopic(self, string):
        self._topic_dict = {
            key: val for key, val in self.topic_dict.items() if val != string
        }

    def pprint(self):
        return '\n'.join([
            "{0}: {1}".format(key, topic)
            for key, topic in self._topic_dict.items()
        ])


ALL_TOPICS = Topics(_topic_dict)
