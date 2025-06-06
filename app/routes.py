from flask import Blueprint, render_template, request, redirect, flash, current_app
from .models import Train
from . import db
import os
from werkzeug.utils import secure_filename
from config import allowed_file

main = Blueprint('main', __name__)

@main.route('/')
def index():
    trains = Train.query.all()
    return render_template('index.html', trains=trains)

@main.route('/train/<int:train_id>')
def train_detail(train_id):
    train = Train.query.get_or_404(train_id)
    return render_template('train_detail.html', train=train)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/delete_train/<int:train_id>', methods=['GET', 'POST'])
def delete_train(train_id):
    train = Train.query.get(train_id)
    if request.method == 'POST':
        if train:
            print('asd')
            db.session.delete(train)
            db.session.commit()
            flash(f"{train.name_en} deleted.")
            return redirect('/')
        else:
            flash("Train not found.")
    
    return render_template('delete_train.html', train=train)

@main.route('/add_train', methods=['GET', 'POST'])
def add_train():
    if request.method == 'POST':
        name_en = request.form.get('name_en')
        name_jp = request.form.get('name_jp')
        description = request.form.get('description')
        region = request.form.get('region')
        operator = request.form.get('operator')
        tags = request.form.get('tags')

        image_file = request.files.get('image_filename')
        image_filename = None

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path) 
            image_filename = filename

        # Create and save the train
        train = Train(
            name_en=name_en,
            name_jp=name_jp,
            description=description,
            image_filename=image_filename,
            region=region,
            operator=operator,
            tags=tags
        )
        db.session.add(train)
        db.session.commit()
        flash("Train added successfully!")
        return redirect('/')
    
    return render_template('add_train.html')

@main.route('/edit_train/<int:train_id>', methods=['GET', 'POST'])
def edit_train(train_id):
    if request.method == 'POST':
        name_en = request.form.get('name_en')
        name_jp = request.form.get('name_jp')
        description = request.form.get('description')
        region = request.form.get('region')
        operator = request.form.get('operator')
        tags = request.form.get('tags')
        image_file = request.files.get('image_filename')
        image_filename = None

        if image_file and allowed_file(image_file.filename) and image_file != train.images:
            filename = secure_filename(image_file.filename)
            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, filename)
            image_file.save(image_path) 
            image_filename = filename


        train = Train.query.get_or_404(train_id)

        train.name_en=name_en,
        train.name_jp=name_jp,
        train.description=description,
        train.image_filename=image_filename,
        train.region=region,
        train.operator=operator,
        train.tags=tags
        
        db.session.add(train)
        db.session.commit()
        return redirect('/train_detail.html')

    return render_template('edit_train.html', train=train)

