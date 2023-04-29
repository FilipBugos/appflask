from azure.data.tables import TableServiceClient, TableClient
import os
from datetime import datetime
import uuid


from flask import Flask, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)

print('app')

# <---------------------------------------------------------------------->

app.config.from_object('config.config')

connection_string = app.config.get('STORAGE_CONNECTION_STRING')
print(connection_string)

# Replace with your connection string and table name
# connection_string = 'DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;'
table_name = 'myTestTable'

# Create a TableServiceClient instance
service_client = TableServiceClient.from_connection_string(connection_string)
try:
    service_client.delete_table(table_name)
    table_client = service_client.create_table_if_not_exists(table_name)
except:
    table_client = service_client.create_table_if_not_exists(table_name)


# Create a TableClient instance for your table

print("Table 'testtable' created.")


# <---------------------------------------------------------------------->


# Insert a new entity into the table
#entity = {
#    'PartitionKey': 'my-partition-key',
#    'RowKey': 'my-row-key',
#    'data': 'Hello, world!'
#}
#table_client.create_entity(entity)

# Retrieve an entity by partition key and row key
#retrieved_entity = table_client.get_entity(partition_key='my-partition-key', row_key='my-row-key')
#print('entity: ')
#print(retrieved_entity)

# Update an existing entity
#updated_entity = {
#    'PartitionKey': 'my-partition-key',
#    'RowKey': 'my-row-key',
#    'data': 'Hello, updated world!'
#}
#table_client.update_entity(mode='replace', entity=updated_entity)

# Delete an entity
#table_client.delete_entity(partition_key='my-partition-key', row_key='my-row-key')

# <----------------------------------------------------------------->

#from models import db, Item


@app.route('/')
def main():
    data = table_client.list_entities(filter=f"PartitionKey eq '{'my-items'}'")
    items = ((item['name'], item['shop'], item['cost']) for item in data)
    headings = ("Name", "Shop", "Cost")
    return render_template('index.html', items=items, headings=headings)

@app.route("/add", methods=['POST'])
def add_item_from_form():
    name = str(request.form['name'])
    shop = str(request.form['shop'])
    cost = str(request.form['cost'])

    new_uuid = uuid.uuid4()

    entity = {
        'PartitionKey': 'my-items',
        'RowKey': str(new_uuid),
        'name': name,
        'shop': shop,
        'cost': cost
    }
    table_client.create_entity(entity)
    
    data = table_client.list_entities(filter=f"PartitionKey eq '{'my-items'}'")
    items = ((item['name'], item['shop'], item['cost']) for item in data)
    headings = ("Name", "Shop", "Cost")
    return render_template('index.html', items=items, headings=headings)

@app.route("/items", methods=['GET'])
def get_items():
    data = table_client.list_entities(filter=f"PartitionKey eq '{'my-items'}'")
    items = ((item['name'], item['shop'], item['cost']) for item in data)
    headings = ("Name", "Shop", "Cost")
    return render_template('index.html', items=items, headings=headings)

#@app.route("/delete")
#def delete_items():
#    db.session.query(Item).delete()
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)