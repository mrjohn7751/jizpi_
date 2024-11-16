from modeltranslation.translator import register, TranslationOptions
from .models import ArticleElon, ArticleNews

@register(ArticleNews)
class ArticleNewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(ArticleElon)
class ArticleElonTranslationOptions(TranslationOptions):
    fields = ('title', 'body')