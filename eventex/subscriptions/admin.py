from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'create_at')
    date_hierarchy = 'create_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'create_at')
    list_filter = ('create_at',)

    def subscribed_today(self):
        return self.create_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)