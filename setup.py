from setuptools import setup, find_packages

setup(
    version='0.0.2',
    name='oasys_devtools',
    author='Pitaia Group',
    description='Oasys plataform devtools',
    packages=find_packages(),
    install_requires=[
        'requests==2.26.0',
        'opencv-python==4.5.3.56'
    ]
)