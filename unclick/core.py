import importlib
import inspect


def convert_type(x):
    if x.isnumeric():
        if x.isdigit():
            return int(x)
        return float(x)
    return x


def get_callable_from_module(module):
    return [x for x, y in module.__dict__.items() if callable(y) and not str(x).startswith('_')]


def show(module):
    for x in get_callable_from_module(module):
        print(str(x))


def run():
    import sys
    if len(sys.argv) < 3:
        raise ValueError("arg0 is <script>.py, arg1 is <func>")
    module_path = sys.argv[1]
    module_function_name = sys.argv[2]
    command_args = sys.argv[3:]
    command_optional_args_idx = len(command_args)
    for i, x in enumerate(command_args):
        if x.startswith('-'):
            command_optional_args_idx = i
            break

    position_args = command_args[:command_optional_args_idx]
    optional_args = command_args[command_optional_args_idx:]
    assert len(optional_args) % 2 == 0

    if module_path.endswith('.py'):
        module_path = module_path[:-3]

    module = importlib.import_module(module_path)
    if module_function_name == 'show':
        show(module)
        return

    if module_function_name == 'args':
        func_name = sys.argv[3]
        try:
            func = module.__dict__[func_name]
        except KeyError:
            raise ValueError(f"func {func_name} not found")

        print(inspect.getfullargspec(func))
        return

    if module_function_name not in module.__dict__:
        raise ValueError(f"function {module_function_name} not found")

    func = module.__dict__[module_function_name]
    if not callable(func):
        raise ValueError(f"f function {module_function_name} is not a python function")

    converted_positional_args = []
    for x in position_args:
        converted_positional_args.append(convert_type(x))

    converted_keyword_args = {}
    for k, v in zip(optional_args[::2], optional_args[1::2]):
        if not k.startswith('--'):
            raise ValueError(f"malformed optional arg: {k}")
        converted_keyword_args[k[2:]] = convert_type(v)

    print(func(*converted_positional_args, **converted_keyword_args))


if __name__ == '__main__':
    run()
