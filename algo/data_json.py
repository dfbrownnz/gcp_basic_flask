
import json
from google.cloud import storage

# https://cloud.google.com/appengine/docs/legacy/standard/python/googlecloudstorageclient/read-write-to-cloud-storage

class c_data_json:

    def __init__(self, file_name):
        self.file_name = file_name
        self.folder_name='C:/Users/dfbro/Desktop/cc/json/'

    def basic_all_json_local_read_write_update(self):
        ma.basic_put()
        ma.basic_add()
        ma.basic_get()

    def basic_get(self):
        print('get')
        # Opening JSON file
        with open(self.folder_name + self.file_name, 'r', encoding='utf-8') as f_in_obj:
            data = json.load(f_in_obj)
            for employee_record in data['employee']:
                print(employee_record)
                for idx_field , val_field in enumerate(dict(employee_record)):
                    print( val_field, employee_record[val_field] )

    def basic_update(self, data):
        employee_record_old={'id': '04', 'name': 'sunil', 'department': 'HR'}
        employee_record_new = {"id": "007", "name": "james", "department": "HR"}
        #del data['employee'][0]
        for employee_idx , employee_record in enumerate(data['employee']):
            if employee_record['name']=='Amit':
                del data['employee'][employee_idx]
        data['employee'].append(employee_record_new)
        return data

    def basic_add(self):
        print('add')
        employee_new={'id': '03', 'name': 'Charlie', 'department': 'CEO'}
        with open(self.folder_name + self.file_name, 'r', encoding='utf-8') as f_in_obj:
            data = json.load(f_in_obj)
            # this adds the new employee to the employee record
            # data["employee"].append({
            #     "id": employee_new['id'] ,
            #     "name": employee_new['name'],
            #     "department": employee_new['department'],
            # })
            data['employee'].append(employee_new)
            data = self.basic_update(data)
            # print(data)

            # this DOES NOT add the new employee to the employee record
            # data = dict(data)
            # data.update( employee_new)
            self.basic_put_data(data)

    def basic_put_data(self, employee_records ):
        with open( self.folder_name + self.file_name,  "w" , encoding='utf-8') as outfile:
            json.dump(employee_records, outfile)

    def basic_put(self):
        # Data to be written
        employee_records= {
            "employee": [

                {
                    "id": "01",
                    "name": "Amit",
                    "department": "Sales"
                },

                {
                    "id": "04",
                    "name": "sunil",
                    "department": "HR"
                }
            ]
        }
        # Serializing json
        json_object = json.dumps(employee_records, indent=4)
        # print(json_object)

        with open( self.folder_name + self.file_name, "w") as outfile:
            json.dump(employee_records, outfile)

        print('put', self.folder_name + self.file_name)

    def gstoreage(self):
        self.authenticate_implicit_with_adc()
        #self.bucket_make()

    from google.cloud import storage

    def authenticate_implicit_with_adc(self, project_id="your-google-cloud-project-id"):
        """
        When interacting with Google Cloud Client libraries, the library can auto-detect the
        credentials to use.

        // T_O_D_O(Developer):
        //  1. Before running this sample,
        //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
        //  2. Replace the project variable.
        //  3. Make sure that the user account or service account that you are using
        //  has the required permissions. For this sample, you must have "storage.buckets.list".
        Args:
            project_id: The project id of your Google Cloud project.
        """

        # This snippet demonstrates how to list buckets.
        # *NOTE*: Replace the client created below with the client required for your application.
        # Note that the credentials are not specified when constructing the client.
        # Hence, the client library will look for credentials using ADC.
        storage_client = storage.Client(project=project_id)
        buckets = storage_client.list_buckets()
        print("Buckets:")
        for bucket in buckets:
            print(bucket.name)
        print("Listed all storage buckets.")

    def bucket_make(self):
        # Imports the Google Cloud client library

        # Instantiates a client
        storage_client = storage.Client()

        # The name for the new bucket
        bucket_name = "my-new-bucket"

        # Creates the new bucket
        bucket = storage_client.create_bucket(bucket_name)

        print(f"Bucket {bucket.name} created.")

    def write_read(self, bucket_name, blob_name):
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your new GCS object
        # blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Mode can be specified as wb/rb for bytes mode.
        # See: https://docs.python.org/3/library/io.html
        with blob.open("w") as f:
            f.write("Hello world")

        with blob.open("r") as f:
            print(f.read())

    def write_read(self, bucket_name, blob_name):
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your new GCS object
        # blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Mode can be specified as wb/rb for bytes mode.
        # See: https://docs.python.org/3/library/io.html
        with blob.open("w") as f:
            f.write("Hello world")

        with blob.open("r") as f:
            print(f.read())

    def list_blobs(self, bucket_name):
        """Lists all the blobs in the bucket."""
        # bucket_name = "your-bucket-name"

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(bucket_name)

        # Note: The call returns a response only when the iterator is consumed.
        for blob in blobs:
            print(blob.name)

    def delete_blob(self, bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        generation_match_precondition = None

        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to delete is aborted if the object's
        # generation number does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = blob.generation

        blob.delete(if_generation_match=generation_match_precondition)

        print(f"Blob {blob_name} deleted.")

if __name__ == '__main__':
    file_name='employee_records.json'
    ma = c_data_json(file_name)
    ma.basic_all_json_local_read_write_update()
    # ma.gstoreage()


