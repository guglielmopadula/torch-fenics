from distutils.core import setup


setup(name='torch-fenics',
      version='0.1',
      description='PyTorch-FEniCS interface',
      author='Patrik Barkman',
      author_email='barkm@kth.se',
      packages=['torch_fenics'],
      install_requires=['dolfin_adjoint,
                        'torch'],
      extras_require={'test': 'pytest'}
      )


