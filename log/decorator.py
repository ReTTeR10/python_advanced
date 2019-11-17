from functools import wraps


class Logger:

    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def _create_message(result=None, *args, **kwargs):
        message = ''
        if args:
            message += f'args: {args} '
        if kwargs:
            message += f'kwargs: {kwargs} '
        if result:
            message += f'= {result}'
        return message

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            # Выполняем функцию и получаем результат
            result = func(*args, **kwargs)
            # Формируем сообщение в лог
            message = Logger._create_message(result, *args, **kwargs)
            # Пишем сообщение в лог
            self.logger.info(f'{message} - {func.__name__} - {func.__module__}')
            return result

        return decorated
