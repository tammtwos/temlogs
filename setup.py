from setuptools import setup, find_packages


def readme():
    with open('E:/smthng/temlogs/README.md', 'r') as f:
        return f.read()


setup(
    name='temlogs',
    version='1.2',
    author='rpelka',
    author_email='tammtwos@gmail.com',
    description='Simple, fast module for logging.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/tammtwos/temlogs',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files log logging fast simple userfriendly',
    project_urls={
        'GitHub': 'https://github.com/tammtwos/temlogs'
    },
    python_requires='>=3.6'
)
