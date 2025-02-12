from flask import Flask, render_template

app = Flask(__name__)



items = [
    {"id": 1, "name": "Item 1", "description": "This is the first item."},
    {"id": 2, "name": "Item 2", "description": "This is the second item."},
    {"id": 3, "name": "Item 3", "description": "This is the third item."},
]




# Route to display a list of items
@app.route('/')
def item_list():
    return render_template('index.html', items=items)

# Route to display details of a specific item
@app.route('/items/<int:item_id>')
def item_detail(item_id):
    # Find the item with the given ID
    item = next((item for item in items if item["id"] == item_id), None)
    
    if item:
        return render_template('view_details.html', item=item)
    else:
        return "Item not found", 404

if __name__ == '__main__':
    app.run(debug=True)