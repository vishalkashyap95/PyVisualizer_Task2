from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="PyVisualizer",
    version="1.0.7",
    description="A simple static visualizer.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/vishalkashyap95/PyVisualizer_Task2.git",
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
    install_requires=["gspread==3.6.0","pandas==0.25.3","requests==2.24.0","matplotlib==3.3.2","seaborn==0.11.0"],
    entry_points={
        "console_scripts": [
            "PyVisualizer=PyVisualizer.Visualizer:__init__",
        ]
    },
)