import os.path

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Генерация пути к файлам-аватарам пользователей
    Формат: TalCloud/media/avatar/user_id/(имя файла)
    """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_image(file_obj):
    """Валидатор размерности файла-аватара"""

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Max size is {megabyte_limit}MB')
