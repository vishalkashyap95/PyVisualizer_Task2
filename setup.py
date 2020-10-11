from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="Visualization_tool",
    version="1.0.0",
    description="A Python package to visualize data via 2D plots.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Vishal Kashyap",
    author_email="vkashyap569@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["PyVisualizer"],
    include_package_data=True,
    install_requires=["gspread","pandas","requests","matplotlib","seaborn"],
    entry_points={
        "console_scripts": [
            "PyVisualizer=PyVisualizer.Visualizer:__init__",
        ]
    },
)