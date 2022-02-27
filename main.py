import modules.arg as arg
import modules.app as app

if __name__ == '__main__':

    cmd = arg.CmdArg()

    path: str = cmd.args.filename
    only: str = cmd.args.only
    exclude: list[str] = cmd.args.exclude
    notab: bool = cmd.args.notab
    leave: bool = cmd.args.leave
    output_name = cmd.args.output
    output_dir = './output/'

    app.main(path, output_name, output_dir, exclude, only, leave, notab)
