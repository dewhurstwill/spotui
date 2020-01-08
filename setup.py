import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotui",
    version="0.1.0",
    author="ceuk",
    description="Spotify TUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="spotify spotifytui",
    url="https://github.com/ceuk/spotui",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.4",
    install_requires=[
        "PySocks==1.7.1",
        "spotipy==2.4.4",
        "windows-curses>=2.0;platform_system=='Windows'",
    ],
    entry_points={"console_scripts": ["spotui=spotui.__main__:main"]},
)
