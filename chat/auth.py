from django.contrib.auth.models import User


def my_authenticate(username,password):
    user = User.objects.filter(username=username).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            print('密码错误！')
            return None
    else:
        print('没有找到此用户')
        return None