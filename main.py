import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcard = Passcard.objects.all()[0]
    print(
        f'''
        Данные из одного пропуска:
        owner_name: {passcard.owner_name}
        passcode: {passcard.passcode}
        created_at: {passcard.created_at}
        is_active: {passcard.is_active}
        '''
    )
