from django import forms
from .models import Article, BlogComment, Suggest


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'body']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入昵称',
                'aria-describedby': 'sizing-addon1',
            }),
            'body': forms.Textarea(attrs={'placeholder': '让我来说两句',
                                          'class': 'form-control',
                                          'rows': 4,
                                          }),
        }


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = ['suggest']
        widgets = {
            'suggest': forms.Textarea(attrs={
                'placeholder': '写下你的意见吧~',
                'class': 'form-control',
                'rows': 4,
                'cols': 80,
                })
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','body','status','abstract','topped','tags']
        widgets = {
            'title':forms.Textarea(attrs={
                'placeholder':'请输入标题',
                'class':'form-control',
                
                'rows':1
            }),
            'body':forms.Textarea(attrs={
                'placeholder':'请输入正文',
                'class':'form-control',
                'rows':15
            }),
            'abstract':forms.Textarea(attrs={
                'placeholder':'请输入摘要',
                'class':'form-control',
                'rows':4
            }),
            
        }