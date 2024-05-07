from setuptools import find_packages, setup

package_name = 'turtlebot_leader'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nicolai',
    maintainer_email='nstall22@student.aau.dk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "camera_subscriber = turtlebot_leader.camera_subscriber:main",
            "lidar_gui = turtlebot_leader.lidar_gui:main",
            "remote_control = turtlebot_leader.remote_control:main"
        ],
    },
)
