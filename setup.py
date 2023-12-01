import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutoropi_plugin_1", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-opi_plugin_1",
    version=ABOUT["__version__"],
    url="https://github.com/myusername/tutor-contrib-opi_plugin_1",
    project_urls={
        "Code": "https://github.com/myusername/tutor-contrib-opi_plugin_1",
        "Issue tracker": "https://github.com/myusername/tutor-contrib-opi_plugin_1/issues",
    },
    license="AGPLv3",
    author="Maciej Komorowski",
    description="opi_plugin_1 plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v1": [
            "opi_plugin_1 = tutoropi_plugin_1.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
