

class TaskPage:
    def __init__(self, page) -> None:
        self.page = page

        """mapping all elements in page"""
        self.task_name_box = page.get_by_label("Name")
        self.task_description_box = page.get_by_label("description")
        self.create_task_button = page.get_by_role("button", name="Create Task")
        self.go_back_button = page.get_by_role("button", name="Back")
        self.task_three_dots = page.get_by_role("button", name="Task Menu")
        self.task_edit_button = page.get_by_role("menuitem", name="Edit")
        self.task_save_button = page.get_by_role("button", name="Save")
        self.task_delete_button = page.get_by_role("menuitem", name="Delete")
        self.task_confirm_delete_button = page.get_by_role("button", name="Confirm Delete")

        # todo complete all elements for future tests

        """actions on the page"""
    def fill_task_name(self, task_name: str):
        self.task_name_box.clear()
        self.task_name_box.fill(task_name)
        print("filling task name")

    def fill_description(self, description: str):
        self.task_description_box.clear()
        self.task_description_box.fill(description)
        print("filling task description")

    def click_create_task(self):
        self.create_task_button.click()
        print("Creating new task")

    def click_go_back(self):
        self.go_back_button.click()

    def click_task_3dot_menu(self):
        self.task_three_dots.click()
        print("open task menu")

    def click_edit_task(self):
        self.task_edit_button.click()
        print("click edit task")

    def click_save_task(self):
        self.task_save_button.click()
        print("click save task")

    def click_delete_button(self):
        self.task_delete_button.click()
        print("click delete button")

    def click_confirm_delete_button(self):
        self.task_confirm_delete_button.click()
        print("click confirm delete")

        # todo complete all actions on page

