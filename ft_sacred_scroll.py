#!/usr/bin/env python3

import alchemy


def main() -> None:
    """Run the main program."""
    print("\n=== Sacred Scroll Mastery ===")
    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"alchemy.create_earth(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as e:
        print(f"alchemy.create_air(): {e.__class__.__name__} - not exposed")
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
