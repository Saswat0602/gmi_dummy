from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()
    start_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    regions = models.TextField()  # Could use JSONField if structured
    address = models.JSONField()
    officers = models.JSONField()
    last_task_num = models.IntegerField(default=0)

    # Link to users with project-specific roles
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='ProjectUserRole',
        related_name='projects'
    )

    def __str__(self):
        return self.name


class ProjectUserRole(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.project.name}"
