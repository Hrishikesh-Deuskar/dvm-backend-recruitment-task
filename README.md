# DVM Backend Task 1 - Django Polls App

This project was made as part of the Department of Visual Media (DVM) backend recruitment task at BITS Pilani.

The project is based on the official Django Polls tutorial. It is a simple polling application where users can view polls, vote for one of the available choices, and view the results.

As an additional feature, I added **categories for polls**, which allow polls to be grouped and viewed based on their category.

## Features

- View the latest polls
- Vote on a poll
- View the results of a poll
- Manage questions and choices using the Django admin page
- Categorize polls into different categories
- View all polls belonging to a particular category
- Django tests for checking application behaviour
- Django Debug Toolbar for inspecting requests and database queries

---

## Additional Feature - Poll Categories

The additional feature I implemented is a category system for polls.

Examples of categories include:

- Sports
- Technology
- Movies
- College
- Other

Each poll can be assigned to a category through the Django admin page.

The category of a poll is displayed along with the poll. Clicking on the category shows all the polls belonging to that particular category.

### Implementation

I created a new `Category` model:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
I then connected the Question model to the Category model using a ForeignKey:

    category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    )

This means that one category can contain multiple questions, while each question can belong to one category.
I also added:
- A category view
- A category URL
- A template for displaying polls from a category
- Category support in the Django admin page
- Category links on the polls pages

Technologies Used
- Python
- Django
- HTML
- CSS
- SQLite
- Django Debug Toolbar