

from currency.tasks import parse_privatbank_archive
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Parse Privatbank Rate archive'
    parse_privatbank_archive()
