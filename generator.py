import datetime
import os

from jinja2 import Environment, FileSystemLoader

TEMPLATES_PATH = 'templates'
TEMPLATE_FILENAME = 'attestation.jinja2.txt'
OUT_FOLDER = '/tmp'  # Only for Linux
OUT_FILENAME = 'attestation.txt'

CHOICE_ACHATS = 'achats'
CHOICES = [
    'pro',
    CHOICE_ACHATS,
    'soins',
    'famille',
    'sport',
    'handicap',
    'judiciaire',
    'mission',
    'enfant'
]
HELP_CHOICES = 'Veuillez choisir entre : ' + ', '.join(CHOICES)
EMPTY_CHOICE = '| |'
FILLED_CHOICE = '|X|'


def _get_template():
    templates_env = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH),
    )
    return templates_env.get_template(TEMPLATE_FILENAME)


def _get_reasons(reason):
    if reason not in CHOICES:
        raise ValueError(f"Votre choix {reason} n'est pas valide. {HELP_CHOICES}")
    reasons = {choice: EMPTY_CHOICE for choice in CHOICES}
    reasons[reason] = FILLED_CHOICE
    return reasons


def _render(template, reason, delta_minutes, notime):
    now = datetime.datetime.now() + datetime.timedelta(minutes=delta_minutes)
    hour = now.strftime('%Hh%M') if notime else ""
    data = {**_get_reasons(reason), **{
        'name': os.environ['DEROG_NAME'],
        'birth_date': os.environ['DEROG_BIRTH_DATE'],
        'birth_place': os.environ['DEROG_BIRTH_PLACE'],
        'address': os.environ['DEROG_ADDRESS'],
        'sign_place': os.environ['DEROG_SIGN_PLACE'],
        'date': now.strftime('%d/%m/%Y'),
        'hour': hour
    }}
    return template.render(**data)


def _save_derogation(output):
    filepath = os.path.join(OUT_FOLDER, OUT_FILENAME)
    with open(filepath, 'w') as f:
        f.write(output)
    return filepath


def generate(reason, delta_minutes, notime):
    template = _get_template()
    output = _render(template, reason, delta_minutes, notime)
    filepath = _save_derogation(output)
    return filepath
