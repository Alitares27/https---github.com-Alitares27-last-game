from constants import *
from game.scene.scene import Scene
from game.scene.scene_manager import SceneManager

def main():
    director = Scene(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()
