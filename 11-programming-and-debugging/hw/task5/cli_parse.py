import argparse
import sys

parser = argparse.ArgumentParser(description='Utility for DDos-attack')

parser.add_argument('-s', '--single',
                    type=int,
                    default=1,
                    help='Single mode DDos, set number of threads')

parser.add_argument('-cl', '--cluster',
                    nargs=1,
                    help='Cluster mode DDos, set -url')

parser.add_argument('-url',
                    choices=['https', 'ssh'],
                    help='Type of cluster-master server')

parser.add_argument('-lf', '--log_file',
                    nargs=1,
                    type=argparse.FileType('w'),
                    default=sys.stdout,
                    help='Set output file')

parser.add_argument('-m', '--mode',
                    choices=['ping', 'long_polling', 'dns_flood'],
                    help='DDos attack mode')

parser.add_argument('-ad', '--address',
                    type=str,
                    required=True,
                    help='Attack server address')

parser.add_argument('-dr', '--dry-run',
                    action='store_true',
                    help='Dry-run mode')

group = parser.add_mutually_exclusive_group()

group.add_argument('-db', '--debug',
                   action='count',
                   default=argparse.SUPPRESS,
                   help='Debug mode')

group.add_argument('-op', '--output',
                   action='store_true',
                   default=True,
                   help='Enable/disable output')

args = parser.parse_args()
address = args.address
debug = args.debug
output = args.output


if not address:
    print('Please input server address')

if debug and output:
    print('Please use only one of args -db or -op')

if args.cluster is None:
    print('Please set type of mode')
elif args.cluster is not None and args.url is None:
    print('Please set type of url cluster-master server with -url')
