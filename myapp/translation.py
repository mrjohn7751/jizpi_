from modeltranslation.translator import register, TranslationOptions
from .models import ArticleElon,ArticleNews

@register(ArticleNews)
class newsTranslationOptions(TranslationOptions):
    fields = ('title','body')
    
    
@register(ArticleElon)
class newsTranslationOptions(TranslationOptions):
    fields = ('title','body')
    
    
