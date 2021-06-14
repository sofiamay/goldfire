
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

# Private
_topic_list = [
    'Intro',
    'Kindness',
    'Discovery',
    'Joy',
    'Shared Sesource',
    'Shadow challenge',
    'Heroic',
    'Action',
]


class Topics:
    # Class attribute:
    all_topics = _topic_list

    def __init__(self, lst):
        self._topic_list = lst

    def __len__(self):
        return len(self._topic_list)

    # FIX
    def __getitem__(self, index):
        return self._topic_list[index]

    def contains(self, string):
        if string in list(self._topic_list):
            return True
        return False

    def add(self, string):
        return self._topic_list.append(string)

    def remove(self, index):
        return self._topic_list.pop(index)

    def removeByTopic(self, string):
        return self._topic_list.remove(string)

    def pprint(self):
        topic_dict = {
            i: self._topic_list[i] for i in range(0, len(self._topic_list))
        }

        return '\n'.join([
            "{0}: {1}".format(key, topic)
            for key, topic in topic_dict.items()
        ])


ALL_TOPICS = Topics(_topic_list)
