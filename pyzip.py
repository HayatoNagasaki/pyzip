# importing module
import pyminizip
import sys


if __name__ == '__main__':
    init_param = {
        'input': './default.txt',
        'output': './default.zip',
        'password': './password',
    }

    if len(sys.argv) >= 3:
        if '--input' in sys.argv:
            init_param['input'] = sys.argv[sys.argv.index('--input') + 1]
        if '--i' in sys.argv:
            init_param['input'] = sys.argv[sys.argv.index('--i') + 1]
        if '--output' in sys.argv:
            init_param['output'] = sys.argv[sys.argv.index('--output') + 1]
        if '--o' in sys.argv:
            init_param['output'] = sys.argv[sys.argv.index('--o') + 1]
        if '--password' in sys.argv:
            init_param['password'] = sys.argv[sys.argv.index('--password') + 1]
        if '--pw' in sys.argv:
            init_param['password'] = sys.argv[sys.argv.index('--pw') + 1]

    if len(sys.argv) < 3 or 'help' in sys.argv:
        help = 'Usage:\n'
        help += '   --input <input file>\n'
        help += '   --i <input file>\n'
        help += '   --output <output file>\n'
        help += '   --o <output file>\n'
        help += '   --password <password>\n'
        help += '   --pw <password>\n'
        help += 'Example1:\n'
        help += '   python pyzip.py --input ./Text.txt --output ./output.zip --password PSW\n'
        help += 'Example2:\n'
        help += '   python pyzip.py --i ./Text.txt --o ./output.zip --pw PSW\n'
        help += '\nIf you are trying to zip a directory,\nyou need to compress whole directory using normal zipper then set password using this.\n'

        print(help)
        exit()

    # input file path
    inp = init_param['input']

    # prefix path
    pre = None

    # output zip file path
    out = init_param['output']

    # set password value
    password = init_param['password']

    # compress level
    com_level = 5

    # compressing file
    pyminizip.compress(inp, None, out,
                       password, com_level)

exit()
