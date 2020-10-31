"""Core > tests > test_tasks.py"""
# PYTHON IMPORTS
import os
import shutil
# DJANGO IMPORTS
from django.conf import settings
from django.test import TestCase
# CORE IMPORTS
from Core.tasks import dbbackup
from Core.tests.utils import suppress_warnings


class TasksTest(TestCase):
    """Test class for testing celery tasks"""
    def setUp(self):
        """setup"""
        self.tmp_file = 'db.bak'
        self.tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')
        if not os.path.exists(self.tmp_dir):
            os.mkdir(self.tmp_dir)

    @suppress_warnings
    def test_dbbackup(self):
        """Tests database backup with celery"""
        self.assertTrue(dbbackup.run(
            path=f"{self.tmp_dir}\\db1.psql.gz"
        ))
        self.assertTrue(dbbackup.run(
            0, 1, path=f"{self.tmp_dir}\\db2.psql"
        ))
        self.assertTrue(dbbackup.run(
            1, 0, path=f"{self.tmp_dir}\\db3.psql.gz"
        ))
        self.assertTrue(dbbackup.run(filename=self.tmp_file))

    def tearDown(self):
        """clean up the temporary folder"""
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

        path = settings.DBBACKUP_STORAGE_OPTIONS.get('location')
        path = path.replace("/", "\\") if os.name == 'nt' else path
        path = os.path.join(settings.BASE_DIR, path)
        path = f"{path}{self.tmp_file}"
        if os.path.exists(path):
            os.remove(path)
