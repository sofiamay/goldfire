from datetime import datetime, timedelta
from topics import Topics
from user import User

# Gathering Model
# gathering_data = {
#     'name': 'Julie\'s Gathering',
#     'date_time': datetime.now(),
#     'total_seats': 4,
#     'time_per_topic': 3,
#     'number_of_topics': 3,
#     'topics': ['kindess', 'heroic', 'action'], -> to set
#     'users': [User.toJSON(), User.toJSON],
#     'available_seats': 2, # property
# }


class Gathering:
    def __init__(self, dict):
        self.name = dict.get('name') or 'An Unnamed Gathering',
        if 'date_time' in dict:
            self.date_time = datetime.fromfromisoformat(dict['date_time'])
        else:
            self.date_time = datetime.now() + timedelta(days=1)
        total_seats = dict.get('total_seats') or 4
        self.total_seats = total_seats
        self.time_per_topic = dict.get('time_per_topic') or 3
        number_of_topics = dict.get('number_of_topics') or 3
        # Topics
        self.number_of_topics = number_of_topics
        if 'topics' in dict:
            topics = set(dict['topics'])
            if len(topics) > number_of_topics:
                raise IndexError(
                    'There are more topics listed than the number of topics'
                )
            for topic in topics:
                if not Topics.isValid(topic):
                    raise ValueError(f'{topic} is not a valid topic')
            self.topics = topics
        else:
            self.topics = set()
        # Users
        if 'users' in dict:
            self.users = [User(userdict) for userdict in dict['users']]
        else:
            self.users = []
        # Properties
        self._available_seats = total_seats

    @property
    def available_seats(self):
        self._available_seats = self.total_seats - len(self.users)
        return self._available_seats

    def isOpen(self):
        return True if len(self.users) < self.total_seats else False

    def toJSON(self):
        return {
            'name': self.name,
            'date_time': self.date_time.isoformat(),
            'total_seats': self.total_seats,
            'time_per_topic': self.time_per_topic,
            'number_of_topics': self.number_of_topics,
            'topics': list(self.topics),
            'users': [user.toJSON() for user in self.users]
        }

    # Override: Method called when printing class
    def __str__(self):
        args = {
            'name': self.name,
            'start_time': self.date_time.strftime('%b %d %H:%M'),
            'total_seats': self.total_seats,
            'available_seats': self.available_seats,
            'time_per_topic': self.time_per_topic,
            'number_of_topics': self.number_of_topics,
            'topics': ', '.join(self.topics),
            'users': ', '.join(self.users),
            'status': 'open' if self.isOpen() else False
        }
        return """{name}:
        \tStart time - {start_time}
        \tTotal seats - {total_seats}
        \tAvailable seats - {available_seats}
        \tTime Per topic - {time_per_topic}
        \tNumber of topicss - {number_of_topics}
        \tTopics - {topics}
        \tMembers joined - {users}
        \tStatus - {status}""".format(**args)
