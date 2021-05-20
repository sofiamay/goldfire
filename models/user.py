# User Model
# {'User':
#     {
#         'name': 'Bob',
#         'id': '122345'
#     }
# }

# Each user has a name and an ID

class User:
    def __init__(self, dict):
        self.username = dict['username']
        self.id = dict['id']

    def toJSON(self):
        return {
            'user': {
                'username': self.username,
                'id': self.id,
            }
        }

    def __str__(self):
        return f'{self.username}'
