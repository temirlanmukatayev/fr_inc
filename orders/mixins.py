class AuthorOnlyMixin:
    '''Allow only authors. Check if current user is the author.'''

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
