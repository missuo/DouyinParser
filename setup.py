'''
Author: Vincent Young
Date: 2022-07-28 19:58:55
LastEditors: Vincent Young
LastEditTime: 2022-07-28 20:26:14
FilePath: /DouyinParser/setup.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
from setuptools import setup, find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="DouyinParser",
    author="missuo",
    version="0.0.3",
    license='MIT',
    long_description= long_description,
    long_description_content_type="text/markdown",
    author_email="i@yyt.moe",
    description="DouyinParser",
    url='https://github.com/missuo/DouyinParser',
    packages=find_packages(),
    include_package_data=False,
    platforms='any',
    zip_safe=False,

    install_requires=[
        'requests'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)