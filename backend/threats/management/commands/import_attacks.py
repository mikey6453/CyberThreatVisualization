import csv
from django.core.management.base import BaseCommand
from threats.models import CyberAttack

class Command(BaseCommand):
    help = 'Import cyber attacks from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Global_Cybersecurity_Threats_2015-2024.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                CyberAttack.objects.create(
                    country=row['Country'],
                    year=int(row['Year']),
                    attack_type=row['Attack Type'],
                    target_industry=row['Target Industry'],
                    financial_loss_million=float(row['Financial Loss (in Million $)']),
                    affected_users=int(row['Number of Affected Users']),
                    attack_source=row['Attack Source'],
                    vulnerability_type=row['Security Vulnerability Type'],
                    defense_mechanism=row['Defense Mechanism Used'],
                    resolution_time_hours=int(row['Incident Resolution Time (in Hours)']),
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported cyber attacks.'))

