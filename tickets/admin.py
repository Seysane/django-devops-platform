from django.contrib import admin
from .models import Ticket
from .models import Comment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "created_by",
        "assigned_to",
        "created_at",
    )

    list_filter = (
        "status",
        "priority",
    )

    search_fields = (
        "title",
        "description",
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "ticket",
        "author",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "content",
        "author__username",
        "ticket__title",
    )

    list_filter = (
        "created_at",
    )