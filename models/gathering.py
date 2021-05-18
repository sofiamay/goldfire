from datetime import datetime, timedelta
from topic import Topic
from user import User

# Gathering Model
# gathering_data = {
#     'date_time': datetime.now(),
#     'total_seats': 4,
#     'time_per_topic': 3,
#     'number_of_topics': 3,
#     'topics': [Topic.kindess, topic.heroic, topic.action], -> to set
#     'users': [User.toJSON(), User.toJSON],
#       'available_seats': 2, # property
# }


class Gathering:
    def __init__(self, dict):
        self.datetime = (
            dict.get('date_time') or datetime.now() + timedelta(days=1))
        total_seats = dict.get('total_seats') or 4
        self.total_seats = total_seats
        self.time_per_topic = dict.get('time_per_topic') or 3
        number_of_topics = dict.get('number_of_topics') or 3
        # Topics
        self.number_of_topics = number_of_topics
        if 'topics' in dict:
            topics = set(
                [Topic.fromJSON(string) for string in dict['topics']]
            )
            if len(topics) > number_of_topics:
                raise IndexError(
                    'There are more topics listed than the number of topics'
                )
            self.topics = topics
        else:
            self.topics = set()
        # Users
        if 'users' in dict:
            self.users = [User(userdict) for userdict in dict['users']]
        else:
            self.users = set()
        # Properties
        self.available_seats = total_seats

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self):
        return self.total_seats - len(self.users)

    # TO DO
    def toJSON(self):
        return
