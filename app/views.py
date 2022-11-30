from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import db, app
from .models import Transactions, User
from .forms import TransactionsForm, UserForm


def transactions_list():
    transaction = Transactions.query.all()
    return render_template('transactions_list.html', transaction=transaction)


@login_required
def transactions_create():
    form = TransactionsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            transactions = Transactions()
            form.populate_obj(transactions)
            db.session.add(transactions)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transactions_form.html', form=form)


def transactions_detail(id):
    transactions = Transactions.query.get(id)
    return render_template('transactions_detail.html', transactions=transactions)


@login_required
def student_update(id):
    transactions = Transactions.query.get(id)
    form = TransactionsForm(request.form, obj=transactions)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(transactions)
            db.session.add(transactions)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transactions_form.html', form=form)


@login_required
def transactions_delete(id):
    transactions = Transactions.query.get(id)
    if request.method == 'POST':
        db.session.delete(transactions)
        db.session.commit()
        flash('transactions успешно удален', 'success')
        return redirect(url_for('transactions_list'))
    return render_template('transactions_delete.html', transactions=transactions)


def register_view():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash(f'поьзователь {user.username} успешно зарегалса', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


def login_view():
    logout_user()
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('успешно авторизован', 'primary')
                return redirect(url_for('transactions_list'))
            else:
                flash('неправильно введенные логин или пароль', 'danger')
    return render_template('login.html', form=form)


def logout_view():
    logout_user()
    return redirect(url_for('login'))
