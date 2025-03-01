from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

class Command(BaseCommand):
    help = "Create user groups and assign permissions"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        permissions = {
            "can_add_book": Permission.objects.get(codename="can_add_book", content_type=content_type),
            "can_view_book": Permission.objects.get(codename="can_view_book", content_type=content_type),
            "can_change_book": Permission.objects.get(codename="can_change_book", content_type=content_type),
            "can_delete_book": Permission.objects.get(codename="can_delete_book", content_type=content_type),
        }

        groups = {
            "Admin": ["can_add_book", "can_view_book", "can_change_book", "can_delete_book"],
            "Librarian": ["can_add_book", "can_view_book", "can_change_book"],
            "Member": ["can_view_book"],
        }

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set([permissions[perm] for perm in perms])
            group.save()
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' updated with permissions"))
