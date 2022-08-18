import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    all_passcards = Passcard.objects.all()
    active_passcards = []
    for passcard in all_passcards:
        if passcard.is_active is True:
            active_passcards.append(passcard)
    print(f'''
    Всего пропусков: {len(all_passcards)}
    Активных пропусков: {len(active_passcards)}
    ''')
