from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aliyun-exporter',
    version='0.3.1',
    description='Alibaba Cloud CloudMonitor Prometheus exporter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aylei/aliyun-exporter',
    author='Aylei Wu',
    author_email='rayingecho@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='monitoring prometheus exporter aliyun alibaba cloudmonitor',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    package_data={'aliyun_exporter': ['static/*','templates/*']},
    install_requires=[
        'prometheus-client',
        'aliyun-python-sdk-cms==7.0.4',
        'aliyun-python-sdk-core-v3==2.13.3',
        'pyyaml',
        'ratelimiter',
        'flask',
        'cachetools',
        'aliyun-python-sdk-ecs==4.16.11',
        'aliyun-python-sdk-rds==2.3.9',
        'aliyun-python-sdk-r-kvstore==2.1.1',
        'aliyun-python-sdk-slb==3.2.10',
        'aliyun-python-sdk-dds==2.0.4',
        'aliyun-python-sdk-vpc==3.0.5',
        'aliyun-python-sdk-cdn==3.0.8',
        'aliyun-python-sdk-domain==3.14.2',
        'aliyun-log-python-sdk==0.6.45',
    ],
    entry_points={
        'console_scripts': [
            'aliyun-exporter=aliyun_exporter:main',
        ],
    },
)
