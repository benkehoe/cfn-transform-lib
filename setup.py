from setuptools import setup

setup(
    name='cfn-transform-lib',
    version='0.1.0',
    description='CloudFormation template transformation',
    packages=["cfn_transform_lib"],
    author='Ben Kehoe',
    author_email='bkehoe@irobot.com',
    project_urls={
        "https://github.com/benkehoe/cfn-transform-lib",
    },
    license='Apache Software License 2.0',
    classifiers=(
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
    ),
    keywords='aws cloudformation',
)