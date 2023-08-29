from setuptools import setup


setup(
    name="indie-scraper",
    version="0.1",
    description="For automating price searching in IndieCampers",
    url="https://github.com/ojp13/indie-scraper",
    author="Oscar Peace",
    author_email="peace.oscar@gmail.com",
    packages=[
        "core"
    ],
    install_requires=[
        "requests==2.29.0"
    ],
    extras_require={
        "development": [
            "debugpy",
        ],
    },
    include_package_data=True,
)
