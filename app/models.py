from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(dp.Sring(255))
    username = db.Column(db.String(255))
    image = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    pitches = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.id}, {self.name}, {self.username}, {self.image}, {self.email}, {self.password}, {self.pitches}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    ratings = db.Column(db.Interger)
    like = db.Column(db.Interger)
    dislike = db.Column(db.Interger)
    content = db.Column(db.String)

    def __repr__(self):
        return f'Comment {self.id}, {self.ratings}, {self.like}, {self.dislike}, {self.content}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    content = db.Column(db.String)
    comment = db.Column(dp.String)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'Pitch {self.id}, {self.category}, {self.title}, {self.author}, {self.content}, {self.comment}'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.column(db.Integer, primary_key=True)
    pitches = db.relationship('Pitch', backref='category')

    def __repr__(self):
        return f'Category {self.id}, {self.pitch}'
