import setuptools

setuptools.setup(
    name="jupyter-tensorboard-proxy",
    version='1.0.1',
    url="https://github.com/sebastiendfortier/jupyter-tensorboard-proxy",
    author="Original: Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy TensorBoard",
    packages=setuptools.find_packages(),
    keywords=['Jupyter', 'TensorBoard'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.3,!=4.0.0,!=4.1.0',
        'tensorboard>=2.15.0',
        'gunicorn>=20.1.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'tensorboard = jupyter_tensorboard_proxy:setup_tensorboard'
        ]
    },
    package_data={
        'jupyter_tensorboard_proxy': ['icons/tensorboard.svg'],
    },
)
