from datetime import datetime, timedelta
from .topics import ALL_TOPICS
from .user import User

# Gathering Model
# gathering_data = {
#     'name': 'Julie\'s Gathering',
#     'date_time': datetime.now(),
#     'total_seats': 4,
#     'time_per_topic': 3,
#     'number_of_topics': 3,
#     'topics': ['Kindess', 'Heroic', 'Action'], -> to set
#     'author': User()
#     'users': [User.toJSON(), User.toJSON],
#     'available_seats': 2, # property
# }


class Gathering:
    def __init__(self, dict):
        self.name = dict.get('name') or 'An Unnamed Circle'
        if 'date_time' in dict:
            self.date_time = datetime.strptime(
                dict['date_time'], '%m-%d-%Y %H:%M'
            )
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
                if not ALL_TOPICS.contains(topic):
                    raise ValueError(f'{topic} is not a valid topic')
            self.topics = topics
        else:
            self.topics = set()
        if 'author' in dict:
            self.author = User(dict['author'])
        else:
            self.author = None
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
            'date_time': self.date_time.strftime('%m-%d-%Y %H:%M'),
            'total_seats': self.total_seats,
            'time_per_topic': self.time_per_topic,
            'number_of_topics': self.number_of_topics,
            'topics': list(self.topics),
            'author': self.author.toJSON(),
            'users': [user.toJSON() for user in self.users]
        }

    def toString(self):
        return self.__str__()

    # Override: Method called when printing class
    def __str__(self):
        args = {
            'name': self.name,
            'start_time': self.date_time.strftime('%m-%d-%Y %H:%M'),
            'total_seats': self.total_seats,
            'available_seats': self.available_seats,
            'time_per_topic': self.time_per_topic,
            'number_of_topics': self.number_of_topics,
            'topics': ', '.join(self.topics),
            'author': self.author.name,
            'users': ', '.join([user.name for user in self.users]),
            'status': 'open' if self.isOpen() else 'closed'
        }
        return """{name}:
        \tStart time - {start_time}
        \tTotal seats - {total_seats}
        \tAvailable seats - {available_seats}
        \tTime Per topic - {time_per_topic}
        \tNumber of topicss - {number_of_topics}
        \tTopics - {topics}
        \tAuthor - {author}
        \tMembers joined - {users}
        \tStatus - {status}""".format(**args)

    @staticmethod
    def isValidName(name):
        if len(name) > 30:
            raise ValueError("Name must be less than 30 characters")
        else:
            return True

    @staticmethod
    def formatDate(date_string):
        date = datetime.strptime(date_string, '%m-%d-%Y %H:%M')
        if date < datetime.now():
            raise ValueError('Date must be in the future')
        return date_string

    @staticmethod
    def isValidTotalSeats(integer_string):
        if not integer_string.isnumeric():
            raise ValueError("Value must be an integer")
        number = int(integer_string)
        if number < 2 or number > 5:
            raise ValueError("Number of participants must be between 2 and 5")
        else:
            return True

    @staticmethod
    def isValidTime(integer_string):
        if not integer_string.isnumeric():
            raise ValueError("Value must be an integer")
        number = int(integer_string)
        if number < 1 or number > 10:
            raise ValueError("Time must be between 1 and 10 minutes")
        else:
            return True

    @staticmethod
    def isValidNumberofTopics(integer_string):
        if not integer_string.isnumeric():
            raise ValueError("Value must be an integer")
        number = int(integer_string)
        if number < 1:
            raise ValueError("You must have at least one topic")
        elif number > 5:
            raise ValueError("You must have less than 6 topics")
        else:
            return True
