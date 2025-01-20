from django.db import models

class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.id} (created at {self.created_at})"
