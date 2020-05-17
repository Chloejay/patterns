import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "boring-project-set-up", 
    version = "0.0.1",
    author = "Chloe Ji",
    author_email = "ji.jie@edhec.com",
    description = "set up boring project to follow the open source project checklist",
    long_description = open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    # packages= ['boring-project-set-up'], 
    python_requires = '>=3.6',
    install_requires = ["setuptools", "docopt"]
)