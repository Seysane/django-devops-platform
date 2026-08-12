from django.contrib.auth.models import User
from django.test import TestCase

from .models import Ticket


class TicketModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

    def test_ticket_creation(self):
        ticket = Ticket.objects.create(
            title="Test ticket",
            description="This is a test ticket.",
            priority=Ticket.Priority.HIGH,
            created_by=self.user,
        )

        self.assertEqual(ticket.title, "Test ticket")
        self.assertEqual(ticket.status, Ticket.Status.OPEN)
        self.assertEqual(ticket.priority, Ticket.Priority.HIGH)
        self.assertEqual(ticket.created_by, self.user)

    def test_ticket_string_representation(self):
        ticket = Ticket.objects.create(
            title="Server is down",
            description="Production server is unavailable.",
            created_by=self.user,
        )

        self.assertEqual(str(ticket), "Server is down")