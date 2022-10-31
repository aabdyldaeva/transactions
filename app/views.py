import datetime

from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Transaction
from .forms import TransactionForm


def index():
    title = 'List of transactions'
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions, title=title)


def transaction_create():
    title = 'Add transaction'
    form = TransactionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_transaction = Transaction()
            form.populate_obj(new_transaction)
            db.session.add(new_transaction)
            db.session.commit()
            flash(f'Transaction # {new_transaction.id} successfully added', 'success')
            return redirect(url_for('transactions'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Error in the field  {field} , error text: {error}', 'danger')
    return render_template('transaction_form.html', form=form, title=title)


def transaction_update(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    form = TransactionForm(request.form, obj=transaction)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(transaction)
            db.session.commit()
            flash(f'Transaction # {transaction_id} updated')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Error in the {field}, error text :  {error}', 'danger')
    return render_template('transaction_form.html', form=form, transaction=transaction)


def transaction_delete(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    form = TransactionForm()
    if request.method == 'GET':
        return render_template('transaction_delete.html', transaction=transaction, form=form)
    if request.method == 'POST':
        db.session.delete(transaction)
        db.session.commit()
        return redirect(url_for('transaction_create'))


def transaction_detail(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    return render_template('transaction_detail.html', transaction=transaction)
