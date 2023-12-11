# from flask import Flask, render_template, request, redirect
# import xml.etree.ElementTree as ET
# import os
# from xml.dom import minidom
# import logging

# app = Flask(__name__)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# XML_FILE = os.path.join(BASE_DIR, "data.xml")

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)

# def load_data():
#     try:
#         tree = ET.parse(XML_FILE)
#         root = tree.getroot()
#     except ET.ParseError as e:
#         logging.error(f"Error parsing XML file: {e}")
#         # Create a new root element if the file is empty
#         root = ET.Element("root")
#         tree = ET.ElementTree(root)
#         tree.write(XML_FILE)
#     return root

# def generate_unique_id(existing_ids):
#     if not existing_ids:
#         return 1
#     else:
#         return max(existing_ids) + 1

# def extract_person_data(person):
#     return {
#         'id': person.findtext('id', default=''),
#         'name': person.findtext('name', default=''),
#         'age': person.findtext('age', default=''),
#         'location': person.findtext('location', default=''),
#         'phone': person.findtext('phone', default=''),
#         'category': person.findtext('category', default=''),
#         'location_event': person.findtext('location_event', default='')
#     }

# def prettify(elem, depth=0):
#     if len(elem):
#         elem.text = '\n' + '\t' * (depth + 1)
#         for sub_elem in elem:
#             prettify(sub_elem, depth + 1)
#         sub_elem.tail = sub_elem.tail[:-1]
#     elem.tail = '\n' + '\t' * depth

# @app.route('/')
# def index():
#     root = load_data()
#     data = [extract_person_data(person) for person in root.findall('person')]
#     return render_template('index.html', persons=data)

# @app.route('/add', methods=['POST'])
# def add():
#     name = request.form['name']
#     age = request.form['age']
#     location = request.form['location']
#     phone = request.form['phone']
#     category = request.form['category']
#     location_event = request.form['location_event']

#     tree = ET.parse(XML_FILE)
#     root = tree.getroot()

#     existing_ids = [int(person.findtext('id', default='')) for person in root.findall('person')]

#     new_id = generate_unique_id(existing_ids)

#     new_person = ET.Element('person')
#     ET.SubElement(new_person, 'id').text = str(new_id)
#     ET.SubElement(new_person, 'name').text = name
#     ET.SubElement(new_person, 'age').text = age
#     ET.SubElement(new_person, 'location').text = location
#     ET.SubElement(new_person, 'phone').text = phone
#     ET.SubElement(new_person, 'category').text = category
#     ET.SubElement(new_person, 'location_event').text = location_event

#     root.append(new_person)
#     prettify(root)

#     tree.write(XML_FILE)

#     return redirect('/')

# @app.route('/search', methods=['GET'])
# def search():
#     search_term = request.args.get('search_id')
#     root = load_data()

#     data = []

#     # Search for a specific user
#     for person in root.findall('person'):
#         if person.findtext('id', default='') == search_term:
#             person_data = extract_person_data(person)
#             data.append(person_data)

#     return render_template('index.html', persons=data)

# @app.route('/update/<int:person_id>', methods=['PATCH', 'POST'])
# def update(person_id):
#     if request.method == 'PATCH':
#         name = request.form['name']
#         age = request.form['age']
#         location = request.form['location']
#         phone = request.form['phone']
#         category = request.form['category']
#         location_event = request.form['location_event']

#         root = load_data()

#         person_to_update = root.find(f"./person[id='{person_id}']")
#         if person_to_update is not None:
#             person_to_update.find('name').text = name
#             person_to_update.find('age').text = age
#             person_to_update.find('location').text = location
#             person_to_update.find('phone').text = phone
#             person_to_update.find('category').text = category
#             person_to_update.find('location_event').text = location_event

#             prettify(root)

#             tree = ET.ElementTree(root)
#             tree.write(XML_FILE)

#         return redirect('/')
#     else:
#         return "Method Not Allowed", 405

# @app.route('/delete/<int:person_id>', methods=['DELETE'])
# def delete(person_id):
#     root = load_data()

#     person_to_delete = root.find(f"./person[id='{person_id}']")
#     if person_to_delete is not None:
#         root.remove(person_to_delete)

#         prettify(root)

#         tree = ET.ElementTree(root)
#         tree.write(XML_FILE)

#     return redirect('/')

# @app.route('/refresh', methods=['GET'])
# def refresh():
#     root = load_data()
#     data = [extract_person_data(person) for person in root.findall('person')]
#     return render_template('index.html', persons=data)

# @app.route('/delete-all', methods=['DELETE'])
# def delete_all():
#     tree = ET.parse(XML_FILE)
#     root = tree.getroot()
    
#     for person in root.findall('person'):
#         root.remove(person)

#     tree.write(XML_FILE)
#     return redirect('/')


import flask
from flask import Flask, render_template
import os

app = Flask(__name__)

# Define the base directory and HTML file path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
HTML_FILE = os.path.join(BASE_DIR, "path/to/your/html/files/index.html")

# Route to render the HTML file
@app.route('/')
def index():
    return render_template(HTML_FILE)

if __name__ == '__main__':
    # Run the app on port 80
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    # Explicitly set the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
