from typing import Callable, Any


class GameScene:
    """
       The base GameScene class.
       You should not use it.
    """

    def __init__(self, name: str, game=None) -> None:
        self.name = name
        self.game = game

    def setup(self):
        pass

    def preload_visible(self):
        pass

    def resize(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def apply_force(self, entities: list[tuple[Any, bool | Callable]], direct: str, force_value):
        """
        entities -> [(entity, condition), (entity, condition)]
        direct - 'N', 'E', 'W', 'S'
        :param entities:
        :param direct:
        :param force_value:
        :return:
        """
        for _ in entities:
            entity = _[0]
            condition = _[1]

            if isinstance(condition, bool):
                if not condition:
                    return
            else:
                if not condition():
                    return

            match direct:

                case 'N': entity.move('up', force_value)

                case 'E': entity.move('right', force_value)

                case 'W': entity.move('left', force_value)

                case 'S': entity.move('down', force_value)

    def on_update(self):
        """
        Modify this function for execute your code while running the game
        :return:
        """
        pass
