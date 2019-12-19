import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hanthon", # Replace with your own username
    version="0.0.1",
    author="flizzywine",
    author_email="1041958497@qq.com",
    description="Write Python in Chinese",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flizzywine/Hanthon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
