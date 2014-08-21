#!/usr/bin/env python
#fileencoding=utf-8

import time
import logging
import hashlib

from scaff import Scaffold

def hash_pwd(pwd, salt):
    return hashlib.sha1(pwd+'|'+salt).hexdigest()[:16]

class Runner(Scaffold):
    def main(self):
        root_user = self.db.user.find_one({'mail': 'root@root'})
        if not root_user:
            root_user = {
                'mail': 'root@root',
                'skype': 'skype',
                'name': 'Bob',
                'alias': 'bob',
                'role': 0,
                'phone': '123456',
                'avatar': 'http://avatar.com/bob',
                'created_at': time.time(),
                'created_by': 'sys',
                'valid': True,
                'join_time': 13897987929,
                'salt': 'dzwOrPqGdgOwBqyV',
            }
            root_user['pwd'] = hash_pwd(hash_pwd('802debaed8f55ffc', root_user['mail']), root_user['salt'])
            self.db.user.insert(root_user)

        logging.info('Start to build index...')
        self.db.user.ensure_index([('mail', 1)], unique=True)
        logging.info('Indexes built.')

if __name__ == '__main__':
    Runner().run()
