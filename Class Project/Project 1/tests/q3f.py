OK_FORMAT = True

test = {   'name': 'q3f',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> 'postal5' in bus.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> (bus['postal5'].str.len() != 5).sum() == 221\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bus['postal5'].isin(valid_zips).sum() == 6032\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bus['postal5'].isna().sum() == 221\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
