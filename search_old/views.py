from django.shortcuts import render
from django.views.generic import ListView

from inventory.models import Asset

class SearchAssetView(ListView):
	template_name = 'search/view.html'

	def get_context_data(self, *args, **kwargs):
		context = super(SearchAssetView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['query'] = query
		return context
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None)
		if query is not None:
			return Asset.objects.search(query)
		return Asset.objects.none()
		# return Asset.objects.featured()
