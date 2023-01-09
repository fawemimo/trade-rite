from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 200
    if file.size > max_size_kb * 1024:
        raise ValidationError('Your file is greater than 50KB')