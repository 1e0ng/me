#!/usr/bin/env python
#fileencoding=utf-8
import logging
import time

import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from scaffold import Scaffold

class Runner(Scaffold):
    def main(self):
        dev_user = self.db.user.find_one({'email': 'debug@local.host'})
        if not dev_user:
            dev_user = {
                'email': 'debug@local.host',
                'skype': 'skype',
                'name': 'Bob',
                'alias': 'bob',
                'role': 0,
                'phone': '123456',
                'avatar': 'http://avatar.com/bob',
                'created_at': time.time(),
                'join_time': 13897987929,
                'pwd' : '802debaed8f55ffc',
                'salt': 'dzwOrPqGdgOwBqyV',
            }
            self.db.user.insert(dev_user)

        logging.info('Start to build index...')
        self.db.user.ensure_index([('mail', 1)], unique=True)
        logging.info('Indexes built.')

if __name__ == '__main__':
    Runner().run()
