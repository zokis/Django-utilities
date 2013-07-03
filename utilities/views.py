# coding: utf-8
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView


class SearchFormListView(FormMixin, ListView):

    '''
    example:
    class UserSearchView(SearchFormListView):
        # initial = {}
        # success_url = None
        # paginate_by = 20
        form_class = UserSearchForm
        model = User

    user_list = login_required(UserSearchView.as_view())

    '''

    def get_form_kwargs(self):
        return {'initial': self.get_initial(), 'data': self.request.GET}

    def get(self, request, *args, **kwargs):
        self.form = self.get_form(self.get_form_class())
        self.object_list = self.form.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
