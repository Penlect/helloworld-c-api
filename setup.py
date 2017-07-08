from setuptools import setup, Extension

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='helloworld-c-api',
    version='1.0.0',
    author='Daniel Andersson',
    author_email='daniel.4ndersson@gmail.com',
    description='Implements a simple Hello World extension module using Python\'s C API',
    long_description=long_description,
    license='MIT',
    keywords='hello world c api extension module',
    url='https://github.com/Penlect/helloworld-c-api',
    ext_modules=[Extension('helloworld',sources=['helloworld.c'])],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: C',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
