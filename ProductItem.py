class ProductItem(db.Model):
    __tablename__ = 'products'


id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(64), unique=True)
descr = db.Column(db.Text, unique=True, nullable=True)
price = db.Column(db.Float, nullable=False)
img = db.Column(db.String(64), unique=True)
cartitems = db.relationship('CartItem', backref='Product')


def __repr__(self):
    return '<ProductName %r>' % self.name

class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    # adding the foreign key
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))