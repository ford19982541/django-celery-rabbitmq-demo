from django.urls import path

from demoq.users.views import (
    generate_random_user,
    get_task_info,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('generate-user/', generate_random_user),
    path('get-task-info/', get_task_info),
]
