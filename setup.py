from setuptools import find_packages, setup

package_name = 'imrc_progress_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/imrc_progress_manager/launch', ['launch/progress_manager.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kei',
    maintainer_email='417keikunv2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'progress_manager = imrc_progress_manager.progress_manager:main'
        ],
    },
)
