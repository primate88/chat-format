from setuptools import setup, find_packages

setup(
    name="PromptRite",
    version="0.0.1",
    author="Charley Darwinson",
    author_email="primate88@proton.me",
    description="A utility to format JSON chat data for LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/primate88/PromptRite",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # install_requires=[
        # "requests>=2.19.1",
    # ],
)