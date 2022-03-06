import modules.arg as arg
import modules.app as app
import importlib

if __name__ == '__main__':

    cmd = arg.CmdArg()
    path = cmd.args.filename
    options_dict = {
        'output':   cmd.args.output,
        'only':     cmd.args.only,
        'excludes': cmd.args.excludes,
        'leave':    cmd.args.leave,
        'notab':    cmd.args.notab,
        'blacket':  cmd.args.blacket,
        'namedeco': cmd.args.namedeco
    }

    if cmd.args.setting is not None:
        toml = importlib.import_module('toml')
        with open(cmd.args.setting, mode='r') as f:
            setting = toml.load(f)
        print(setting)
        for k, v in setting['options'].items():
            options_dict[k] = v

    app.main(path, options_dict)
