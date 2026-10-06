# game/scripts/00_systems.rpy
init python early:
    import sys
    import os
    import renpy.config as config

    # Append custom python module path
    python_dir = os.path.join(config.gamedir, "python")
    if python_dir not in sys.path:
        sys.path.append(python_dir)

    # Import modules directly
    import game_state
    import stat_checks