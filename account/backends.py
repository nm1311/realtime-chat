from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

"""
I don't know how its working. It works for any USERNAME_FIELD to make it case insensitive.
(https://codingwithmitch.com/courses/real-time-chat-messenger/custom-user-model/   at  34:00)
(Look into it later)
"""

class CaseInsensitiveModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})

        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        
        else:
            if user.check_password and self.user_can_authenticate(user):
                return user