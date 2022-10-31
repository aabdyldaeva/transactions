from .views import app, index, transaction_create, transaction_delete, transaction_update, transaction_detail

app.add_url_rule('/transaction/create', view_func=transaction_create, methods=['GET','POST'], endpoint='transaction_create')
app.add_url_rule('/transaction/<int:transaction_id>', view_func=transaction_detail, methods=['GET', 'POST'], endpoint='transaction_detail')
app.add_url_rule('/transaction/update', view_func=transaction_update, methods=['GET', 'POST'], endpoint='transaction_update')
app.add_url_rule('/transaction/<int:transaction_id>/delete', view_func=transaction_delete, methods=['GET', 'POST'], endpoint='transaction_delete')


app.add_url_rule('/', view_func=index, methods=['GET', ], endpoint='transactions')
