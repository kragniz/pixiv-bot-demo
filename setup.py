import setuptools

setuptools.setup(
    name="pixiv-bot-demo",
    version="0.1.0",
    url="https://github.com/kragniz/pixiv-bot-demo",

    author="Louis Taylor",
    author_email="louis@kragniz.eu",

    description="A demo pixiv bot to dogfood python-pixiv",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
