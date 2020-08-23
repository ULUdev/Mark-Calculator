from setuptools import setup
setup(
    name = "markmanager",
    version= "0.0.1",
    packages= ["clicode"],
    entry_points={
        "console_scripts": [
            "markmanager = clicode.cmd:main"
        ]
    }
)