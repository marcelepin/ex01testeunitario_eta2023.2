class User:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __repr__(self):
        return f"User(name={self.name}, job={self.job})"
