from django.contrib import admin

from commerce.models import (

    Label,  service,center,notification,advertising, Center_image,Service_image,ServiceOpinion,CenterOpinion,reservation,

)
"""class InlineProductImage(admin.TabularInline):
    model = ProductImage"""


"""class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'qty', 'description', 'cost', 'price', 'discounted_price')
    list_filter = ('category', 'label', 'merchant', 'vendor')
    search_fields = ('name', 'qty', 'description', 'cost', 'price', 'discounted_price', 'merchant__name')
"""

admin.site.register(Label)
admin.site.register(service)
admin.site.register(center)
admin.site.register(notification)
admin.site.register(advertising)
admin.site.register(Service_image)
admin.site.register(Center_image)
admin.site.register(reservation)


class Service_opinionAdmin(admin.ModelAdmin):
    list_display = ('id','description','time')

class Center_opinionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'time')

admin.site.register(ServiceOpinion,Center_opinionAdmin)
admin.site.register(CenterOpinion,Center_opinionAdmin)
