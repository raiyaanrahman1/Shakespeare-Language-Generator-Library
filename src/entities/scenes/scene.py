class Scene:
    num_scenes = 0

    def __init__(self, characters) -> None:
        if len(characters) != 2:
            raise Exception('scenes must have exactly two characters')
        
        self.characters = characters

        Scene.num_scenes += 1
        self.id = Scene.num_scenes