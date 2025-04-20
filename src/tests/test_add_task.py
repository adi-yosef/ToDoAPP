from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page, create_new_task_sidebar
import pytest

pytestmark = [pytest.mark.ui, pytest.mark.new_task]

def test_add_task_from_home_page(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()


def test_add_task_from_sidebar(page):
    create_new_task_sidebar("adi2","my 2nd test", page)
    expect(page.get_by_role("heading", name="adi2")).to_be_visible()



