from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page
from src.steps.edit_existing_task import edit_existing_task

import pytest
pytestmark = [pytest.mark.ui, pytest.mark.edit_task]

def test_edit_task(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    edit_existing_task("adi",page, "my new task name", "my new description")