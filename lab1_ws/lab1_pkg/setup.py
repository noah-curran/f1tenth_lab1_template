from setuptools import setup

package_name = 'lab1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ntcurran',
    maintainer_email='ntcurran@umich.edu',
    description='TODO',
    license='TODO',
    tests_require=['pytest'],
    entry_points = {
        'console_scripts': [
            'minimal_python_node = lab1_pkg.lab1_node:main',
            'test_node = lab1_pkg.my_first_node:main',
            'talker = lab1_pkg.talker:main',
            'relay = lab1_pkg.relay:main',
        ],
    },
)
