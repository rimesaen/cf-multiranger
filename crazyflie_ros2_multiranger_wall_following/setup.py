from setuptools import find_packages, setup

package_name = 'crazyflie_ros2_multiranger_wall_following'
submodule_name = 'crazyflie_ros2_multiranger_wall_following/wall_following'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodule_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kimberly McGuire',
    maintainer_email='kimberly@bitcraze.io',
    description='Wall following for Crazyflie using multiranger data',
    license='MIT',
    entry_points={
        'console_scripts': [
            'single_multiranger = crazyflie_ros2_multiranger_wall_following.single_multiranger:main',
            'single_camera_multiranger = crazyflie_ros2_multiranger_wall_following.single_camera_multiranger:main',
            'double_multiranger = crazyflie_ros2_multiranger_wall_following.double_multiranger:main',
            'double_camera_multiranger = crazyflie_ros2_multiranger_wall_following.double_camera_multiranger:main'
        ],
    },
)
