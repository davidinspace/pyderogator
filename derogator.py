import os
import subprocess

import click

from generator import generate, CHOICE_ACHATS, HELP


DEFAULT_DELTA_MINUTES = int(os.environ.get('DEROG_DELTA_MINUTES', 5))


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
@click.option('--minutes', default=DEFAULT_DELTA_MINUTES, help="Minutes a ajouter a l'heure courante")
def derogate(reason, minutes):
    filepath = generate(reason, minutes)
    fileuri = 'file://' + filepath
    print(f"derogation {reason} (+{minutes}m) : {fileuri}")
    print_file(filepath)
    print('')
    tell_fortune()


if __name__ == '__main__':
    derogate()
