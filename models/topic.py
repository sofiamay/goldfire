
# {
#     'topics': ['joy', 'intro', 'kindness']
# }

class Topic:
    intro = 'intro'
    kindness = 'kindness'
    discovery = 'discovery'
    joy = 'joy'
    shared_resource = 'shared resource'
    shadow_challenge = 'shadow challenge'
    heroic = 'heroic'
    action = 'action'

    @classmethod
    def fromJSON(cls, string):
        if string == 'intro':
            return cls.intro
        elif string == 'kindness':
            return cls.kindness
        elif string == 'discovery':
            return cls.discovery
        elif string == 'joy':
            return cls.joy
        elif string == 'shared resource':
            return cls.shared_resource
        elif string == 'shadow challenge':
            return cls.shadow_challenge
        elif string == 'heroic':
            return cls.heroic
        elif string == 'action':
            return cls.action
        else:
            return

    # TO DO
    @classmethod
    def toJSON(cls, string):
        return
