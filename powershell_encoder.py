import sys, argparse, base64

parser = argparse.ArgumentParser()
parser.add_argument('command', nargs='?', help='String to encode', type=str)
parser.add_argument('-s', '--stdin', default=False, help='Reading from stdin', action='store_true')
args = parser.parse_args()

if args.stdin == True:
	payload = sys.stdin.read().encode('utf-8')
elif args.command:
	payload = args.command.encode('utf-8')
else:
	sys.exit(parser.print_help())


encoded_strings = ''
for chars in payload:
	encoded_strings += chars + "\x00"


print(base64.b64encode(encoded_strings))
