import setuptools 

with open("README.md","r",encoding = "urf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "NavnathAvate1234"
SRC_REPO = "cnnClassifier"
AUTHOP_EMAIL = "awatenavnath39@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description= "A small python package for CNN app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHEOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
    
)