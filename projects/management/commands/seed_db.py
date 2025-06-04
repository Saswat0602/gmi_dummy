import json
import random
import uuid
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from projects.models import Project, ProjectUserRole
from sheets.models import Sheet
from photos.models import Photo, PhotoAnnotation
from reports.models import Report, Sign
from versionsheets.models import VersionSheet
from tasks.models import Task, Stamp
from documents.models import Document
from authflow.models import EmailToken

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        self.clear_data()

        try:
            self.stdout.write("Creating users...")
            users = self.create_users()

            self.stdout.write("Creating projects...")
            projects = self.create_projects(users)

            self.stdout.write("Creating version sheets...")
            versionsheets = self.create_version_sheets(projects)

            self.stdout.write("Creating sheets...")
            sheets = self.create_sheets(projects, versionsheets, users)

            self.stdout.write("Creating photos...")
            photos = self.create_photos(projects, sheets, users)

            self.stdout.write("Creating documents...")
            self.create_documents(projects)

            self.stdout.write("Creating photo annotations...")
            self.create_photo_annotations(photos, projects, users)

            self.stdout.write("Creating reports...")
            reports = self.create_reports(projects, photos, users)

            self.stdout.write("Creating signs...")
            self.create_signs(reports, users)

            self.stdout.write("Creating stamps...")
            stamps = self.create_stamps(projects)

            self.stdout.write("Creating tasks...")
            self.create_tasks(projects, sheets, reports, photos, stamps, users)

            self.stdout.write("Creating project user roles...")
            self.create_project_user_roles(projects, users)

            self.stdout.write("Creating email tokens...")
            self.create_email_tokens(users)

            self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Seeding failed: {e}"))

    def clear_data(self):
        EmailToken.objects.all().delete()
        Task.objects.all().delete()
        Stamp.objects.all().delete()
        Sign.objects.all().delete()
        Report.objects.all().delete()
        PhotoAnnotation.objects.all().delete()
        Photo.objects.all().delete()
        Sheet.objects.all().delete()
        VersionSheet.objects.all().delete()
        Document.objects.all().delete()
        ProjectUserRole.objects.all().delete()
        Project.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

    def create_users(self):
        users = []
        for i in range(1, 6):
            user = User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='password123',
                fullname=f'User {i}',
                role='member',
                is_verified=True,
                first_name=f'First{i}',
                last_name=f'Last{i}',
            )
            users.append(user)
        return users

    def create_projects(self, users):
        projects = []
        for i in range(1, 6):
            project = Project.objects.create(
                name=f'Project {i}',
                num=i,
                start_date=datetime.today().date() - timedelta(days=30 * i),
                status=True,
                regions='Region1, Region2',
                address={"street": "123 Main St", "city": "City", "zip": "12345"},
                officers={"officer1": "Name1", "officer2": "Name2"},
                last_task_num=0
            )
            project.users.set(users[:3])  # Assign first 3 users
            projects.append(project)
        return projects

    def create_version_sheets(self, projects):
        versionsheets = []
        for i, project in enumerate(projects):
            vs = VersionSheet.objects.create(
                id=uuid.uuid4(),
                project=project,
                name=f'Version Sheet {i + 1}',
                issuance_date=timezone.now().date()
            )
            versionsheets.append(vs)
        return versionsheets

    def create_sheets(self, projects, versionsheets, users):
        sheets = []
        for i in range(5):
            sheet = Sheet.objects.create(
                project=projects[i % len(projects)],
                version_sheet=versionsheets[i % len(versionsheets)],
                dpi='300',
                num=f'Sheet-{i + 1}',
                name=f'Sheet Name {i + 1}',
                tags={"tag1": "value1"},
                width='1000',
                height='1500',
                pdf_url='http://example.com/pdf.pdf',
                page_index=0,
                plan_set_id=uuid.uuid4(),
                full_img_url='http://example.com/full_img.png',
                version_set_id=uuid.uuid4(),
                plan_set_s3_url='http://example.com/s3url.png',
                thumbnail_url='http://example.com/thumb.png',
                plan_set_filename='filename.pdf',
                text_extract_data_url='http://example.com/text_extract',
                text_detect_full_page_url='http://example.com/text_detect',
                uploaded_by=users[i % len(users)],
            )
            sheets.append(sheet)
        return sheets

    def create_photos(self, projects, sheets, users):
        photos = []
        for i in range(5):
            photo = Photo.objects.create(
                project=projects[i % len(projects)],
                url=f'http://example.com/photo{i}.jpg',
                raw_url=f'http://example.com/raw_photo{i}.jpg',
                default_url=f'http://example.com/default_photo{i}.jpg',
                large_url=f'http://example.com/large_photo{i}.jpg',
                thumbnail_url=f'http://example.com/thumb_photo{i}.jpg',
                title=f'Photo Title {i + 1}',
                tags={"tag": f"value{i+1}"},
                filename=f'photo{i}.jpg',
                modified_at=timezone.now(),
                uploaded_by=users[i % len(users)],
                is_temporarily_present=False,
                is_annotation=False,
            )
            photo.sheets.set(sheets[i % len(sheets): (i % len(sheets)) + 2])
            photos.append(photo)
        return photos

    def create_documents(self, projects):
        for i in range(5):
            Document.objects.create(
                project=projects[i % len(projects)],
                s3Url='http://example.com/s3url',
                file_url='http://example.com/file_url',
                name=f'Document {i + 1}',
                dirPath='',
                description=f'Description for document {i + 1}',
                filename=f'doc{i+1}.pdf',
                file_type='pdf',
                file_size=12345,
            )

    def create_photo_annotations(self, photos, projects, users):
        for i in range(5):
            PhotoAnnotation.objects.create(
                photo=photos[i % len(photos)],
                project=projects[i % len(projects)],
                user=users[i % len(users)],
                published=bool(i % 2),
                type='rectangle',
                shape_data={"x": i * 10, "y": i * 20, "width": 100, "height": 50},
            )

    def create_reports(self, projects, photos, users):
        reports = []
        for i in range(5):
            report = Report.objects.create(
                project=projects[i % len(projects)],
                name=f'Report {i + 1}',
                template_id=str(uuid.uuid4()),
                status='draft',
                data={"field": f"value{i+1}"},
                published=bool(i % 2),
                created_by=users[i % len(users)],
                updated_by=users[(i + 1) % len(users)],
            )
            report.photos.set(photos[i % len(photos): (i % len(photos)) + 2])
            reports.append(report)
        return reports

    def create_signs(self, reports, users):
        for i in range(5):
            Sign.objects.create(
                report=reports[i % len(reports)],
                Key=f'Key-{i + 1}',
                user=users[i % len(users)],
                rawUrl='http://example.com/raw_sign.png',
                thumbnailUrl='http://example.com/thumb_sign.png',
                name=f'Signer {i + 1}',
                file_url='http://example.com/file_sign.png',
            )

    def create_stamps(self, projects):
        stamps = []
        for i in range(5):
            stamp = Stamp.objects.create(
                project=projects[i % len(projects)],
                name=f'Stamp {i + 1}',
                image_url=f'http://example.com/stamp{i}.png',
            )
            stamps.append(stamp)
        return stamps

    def create_tasks(self, projects, sheets, reports, photos, stamps, users):
        for i in range(5):
            task = Task.objects.create(
                project=projects[i % len(projects)],
                sheet=sheets[i % len(sheets)],
                report=reports[i % len(reports)],
                stamp=stamps[i % len(stamps)],
                type='type_example',
                title=f'Task Title {i + 1}',
                list_id=f'list_{i + 1}',
                status='open',
                task_num=i + 1,
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=7),
                description=f'Task description {i + 1}',
                created_by=users[i % len(users)],
            )
            task.assigned_to.set(users[:2])
            task.watching.set(users[2:4])

    def create_project_user_roles(self, projects, users):
        roles = ['manager', 'member', 'viewer']
        for i, project in enumerate(projects):
            for j, user in enumerate(users[:3]):
                if not ProjectUserRole.objects.filter(project=project, user=user).exists():
                    ProjectUserRole.objects.create(
                        project=project,
                        user=user,
                        role=roles[(i + j) % len(roles)]
                    )

    def create_email_tokens(self, users):
        for i, user in enumerate(users):
            EmailToken.objects.create(
                user=user,
                token=uuid.uuid4(),
                token_type=EmailToken.EMAIL_VERIFICATION if i % 2 == 0 else EmailToken.PASSWORD_RESET,
            )
