from .action import Action


class GoToAction(Action):
    # Currently only supports one act
    def __init__(self, scene_num) -> None:
        super().__init__(f"Let us return to scene {scene_num}")
