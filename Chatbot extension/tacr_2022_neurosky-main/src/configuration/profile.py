import yaml


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Ensure profile yaml properties save/load
# used for the configuration of variables
class Profile(metaclass=Singleton):

    def __init__(self, path=r'..\profile.yaml'):
        self.profile_path = path
        self.profile = self.read_profile()

    def get_profile(self):
        return self.profile

    def set_profile(self, profile):
        self.profile = profile
        self.write_profile()

    def read_profile(self):
        with open(self.profile_path) as file:
            profile = yaml.load(file, Loader=yaml.FullLoader)
            return profile

    def write_profile(self):
        with open(self.profile_path, 'w') as file:
            profile = yaml.dump(self.profile, file)

    def write(self, variable, value):
        self.profile[variable] = value
        self.write_profile()
