OK_FORMAT = True

test = {   'name': 'q1a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(bike, pd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bike['holiday'].dtype == np.dtype('O')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bike['weekday'].dtype == np.dtype('O')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bike['workingday'].dtype == np.dtype('O')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bike['weathersit'].dtype == np.dtype('O')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
