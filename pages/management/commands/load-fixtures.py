from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command("makemigrations")  
        call_command("migrate")
        call_command("loaddata", "navlink.json")
        # call_command("loaddata", "db_mainbanner.json")
        # call_command("loaddata", "db_navlink.json")
        # call_command("loaddata", "db_navlinkitem.json")
        # call_command("loaddata", "db_sectionbanner.json")
        # call_command("loaddata", "db_seo_optimization.json")
        # call_command("loaddata", "db_testimonial.json")
        # call_command("loaddata", "db_topbar.json")
