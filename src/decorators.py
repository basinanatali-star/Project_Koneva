import functools


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def decorator(func):
        """Декоратор, который сохраняет метаданные о функции"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log_message = []
                # результат выполнения заданной функции
                result = func(*args, **kwargs)
                # вывод результата успешного выполнения функции в консоль, если filename не задан
                log_message.append("my_function ok")
                output = " ".join(log_message)
                # вывод результата успешного выполнения функции в файл, если filename задан
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(output + " ")
                else:
                    print(output)
                return result
            # вывод результата выполнения функции с ошибкой в консоль, если filename не задан
            except Exception as e:
                log_message.append(f"my_function error: {e}. Inputs: {args},{kwargs} ")
            output = " ".join(log_message)
            # вывод результата выполнения функции с ошибкой в файл, если filename задан
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(output + " ")
            else:
                print(output)
            raise

        return wrapper

    return decorator
