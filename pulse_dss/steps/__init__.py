import notebooks.loader as loader
import notebooks.user


class Step:
    def __init__(self, name):
        self._name = name
        print(notebooks.user)

    def execute(self, df):
        pass


if __name__ == '__main__':
    loader.configure()
    Step('new')
