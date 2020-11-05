import os
import subprocess

import click

from generator import generate, CHOICE_ACHATS, HELP


def print_file(filepath):
    """
    Only for Linux
    """
    printer = os.environ.get('DEROG_PRINTER')
    if not printer:
        print('No printer configured (see README)')
        return

    command = f'lpr -P {printer} {filepath}'
    result = os.system(command)
    if result != 0:
        print(f'Unknown printer error for {command}')
    else:
        print('printed :)')


def tell_fortune():
    """
    Only for Linux
    Please see README to make it work
    """
    try:
        # Use subprocess to avoid an error if
        # the programs are not installed
        subprocess.run('fortune | cowsay', shell=True)
    except Exception as ex:
        pass


@click.command()
@click.option('--reason', default=CHOICE_ACHATS, help=HELP)
def derogate(reason):
    delta_minutes = int(os.environ.get('DEROG_DELTA_MINUTES', 5))
    filepath = generate(reason, delta_minutes)
    fileuri = 'file://' + filepath
    print(f"derogation {reason} (+{delta_minutes}m) : {fileuri}")
    print_file(filepath)
    print('')
    tell_fortune()


if __name__ == '__main__':
    derogate()
