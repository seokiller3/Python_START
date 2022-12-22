from datetime import datetime


def log(func):
    def wrapper(*args):
        with open('log.csv', 'a', encoding='utf-8') as log_file:
            log_file.write(
                f'{datetime.now()} – запущена функция {func.__name__} {f"с аргументами: {args}" if args else "без аргументов"} ({func.__doc__})\n')

        return func(*args)

    return wrapper
