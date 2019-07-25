from django.shortcuts import render
from django.views import generic

from inventory.models import Asset

from carts.models import AssetCart


class SearchAssetsIndexView(generic.ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchAssetsIndexView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Asset.objects.search(query)
        # return Asset.objects.active()
        # TODO: This does not work yet
        return Asset.objects.all()
