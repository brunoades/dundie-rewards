from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="dundie-rewards-system",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Bruno A de Souza",
    packages=find_packages(),
<<<<<<< Updated upstream
)
=======
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)
>>>>>>> Stashed changes
