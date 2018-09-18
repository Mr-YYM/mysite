import re

from django import forms
from django.contrib.auth import get_user_model


def lowercase_email(email):
    """
    Normalize the address by lowercasing the domain part of the email
    address.
    """
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = '@'.join([email_name.lower(), domain_part.lower()])
    return email


class SignUpForm(forms.ModelForm):
    """
    创建字段:

    class Field(**kwargs)
    When you create a Form class, the most important part is defining the fields of the form.
    Each field has custom validation(校验) logic, along with a few other hooks.
    """

    # ........

    """
    每个Field的clean()函数:
    
    Field.clean(value)
    Although the primary way you'll use Field classes is in Form classes,
    you can also instantiate them and use them directly to get a better idea of how they work.
    Each Field instance has a clean() method,
    中文解释：通常Field在Form的子类中使用，但我们也可以将他们实例化，利用clean()函数检验value值是否符合字段（的格式）要求。
    
    which takes a single argument and either raises a django.forms.ValidationError exception or
    returns the clean value:
    中文解释：clean() 接收一个参数value，符合要求的直接返回原来的value的内容，不符合的抛出ValidationError异常
    
        >>> from django import forms
        >>> f = forms.EmailField()
        >>> f.clean('foo@example.com')
        'foo@example.com'
        >>> f.clean('invalid email address')
        Traceback(most recent call last):
        ...
        ValidationError: ['Enter a valid email address.']
        
    """

    username = forms.CharField(  # 接收字符型数据

        # Core field arguments

        # label: The label argument lets you specify the "human-friendly" label for this field.
        #        This is used when the Field is displayed in a Form.
        #        给我们自己看的
        label='用户名',

        # required: By default, each Field class assumes the value is required,
        #           so if you pass an empty value
        #           -- either None or the empty string ("")
        #           -- then clean() will raise a ValidationError exception:
        #           If a Field has required=False and you pass clean() an empty value,
        #           then clean() will return a normalized empty value rather than raising ValidationError.
        #           For CharField, this will be an empty string('').
        #           For other Field classes, it might be None. (This varies from field to field.)
        #           必填值，默认True。
        #           必填(required=True)没填的抛出ValidationError;
        #           非必填(required=False)，CharField返回''，其余的返回None.
        required=True,

        # max_length，min_length: 最长最短
        max_length=15, min_length=3,

        # widget: The widget argument lets you specify a Widget class to use when rendering this Field.
        # CSS 的东西，跟前端有关
        widget=forms.TextInput(attrs={'placeholder': '3~15位字母/数字/汉字'}),

        # error_messages: The error_messages argument lets you override the default messages that the field will raise.
        # Pass in a dictionary with keys matching the error messages you want to override.
        # default error message: ValidationError: ['This field is required.']
        # custom error message: ValidationError: ['your custom error message']
        # 自定义报错信息
        error_messages={'required': '请填写你的用户名',
                        'max_length': '最多只能输入15个字符',
                        'min_length': '至少输入3个字符'}
        )

    email = forms.EmailField(
        label='邮箱', required=True,
        widget=forms.EmailInput(attrs={'placeholder': '填写正确的email以便激活你的账户'}),
        error_messages={'required': '请填写你的email',
                        'invalid': 'email格式不正确'}
        )

    password = forms.CharField(
        label='密码', required=True, max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}),
        error_messages={'required': '请输入密码',
                        'max_length': '最多只能输入20个字符',
                        'min_length': '至少输入6个字符'}
        )

    confirm_password = forms.CharField(
        label='确认密码', required=True, max_length=20, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '长度在6~20个字符以内'}),
        error_messages={'required': '请输入密码',
                        'max_length': '最多只能输入20个字符',
                        'min_length': '至少输入6个字符'}
        )

    class Meta:
            model = get_user_model()
            fields = ("username", "email", "password",)

    def clean_email(self):
        UserModel = get_user_model()  # Return the User model that is active in this project.
        email = self.cleaned_data["email"]
        lower_email = lowercase_email(email)
        try:
            UserModel._default_manager.get(email=lower_email)
        except UserModel.DoesNotExist:
            return lower_email
        raise forms.ValidationError("有人已经注册了这个email地址")

    def clean_confirm_password(self):
        # cleaned_data=super(SignupForm,self).clean()
        password = self.cleaned_data.get("password", False)
        confirm_password = self.cleaned_data["confirm_password"]
        if not (password == confirm_password):
            raise forms.ValidationError("确认密码和密码不一致")
        return confirm_password

    def clean_username(self):
        UserModel = get_user_model()
        username = self.cleaned_data["username"]
        # 过滤用户名敏感词的注册用户
        n = re.sub('^\u4e00-\u9fa5a-zA-Z', '', username)

        mgc = ['admin', 'fanhuaxiu', '繁花社长']

        if n in mgc:
            raise forms.ValidationError("这么好的名字当然被人提前预定啦，换一个试试^-^")

        try:
            UserModel._default_manager.get(username=username)

        except UserModel.DoesNotExist:
            return username
        raise forms.ValidationError("有人已经注册了这个用户名")
