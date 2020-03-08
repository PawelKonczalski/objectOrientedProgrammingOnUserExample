class User:
    name = 'none'
    next_id = 1

    def __init__(self, name=''):
        self.name = name
        self.id = User.next_id
        User.next_id += 1
