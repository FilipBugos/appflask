import os

#conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
#conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

#DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:5432/{dbname}'.format(
#    dbuser=conn_str_params['user'],
#    dbpass=conn_str_params['password'],
#    dbhost=conn_str_params['host'],
#    dbname=conn_str_params['dbname']
#)


conn_str = os.environ['AZURE_STORAGE_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(';')}

end_str = os.environ['AZURE_STORAGE_ENDPOINTS']
end_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in end_str.split(';')}

IS_EMULATED = False
STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName={accountname};AccountKey={key};EndpointSuffix=core.windows.net;BlobEndpoint={blobE};TableEndpoint={tableE};QueueEndpoint={queeE};'.format(
    accountname=conn_str_params['AccountName'],
    key=conn_str_params['AccountKey'],
    blobE=end_str_params['BlobEndPoint'],
    tableE=end_str_params['TableEndPoint'],
    queeE=end_str_params['QueueEndPoint']
)