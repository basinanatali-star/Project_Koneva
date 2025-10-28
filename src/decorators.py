import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log_message = []
                result = func(*args, **kwargs)
                log_message.append("my_function ok")
                output = " ".join(log_message)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(output + " ")
                else:
                    print(output)
                return result

            except Exception as e:
                log_message.append(f"my_function error: {e}\n")
            output = " ".join(log_message)
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(output + " ")
            else:
                print(output)
            raise

        return wrapper

    return decorator
