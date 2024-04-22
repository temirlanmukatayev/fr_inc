from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """Views decorator. Checks that logged in user is a client. Redirects to the
    login page if necessary."""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_client,
        login_url='/users/login/',
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def worker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """Views decorator. Checks that logged in user is a worker. Redirects to the
    login page if necessary."""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_worker,
        login_url='/users/login/',
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
