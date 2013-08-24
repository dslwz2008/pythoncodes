#!/usr/bin/env python 
# -*- coding:utf-8 -*- 

import boto
from boto.s3.connection import Location
import datetime

bucket_name = 'jyblogpicturebucket'
#print dir(Location)

def createbucket(bucket_name, location = Location.APNortheast):
    conn = boto.connect_s3()
    bucket = conn.create_bucket(bucket_name, location = location)
    print bucket
    
def listkeys():
    conn = boto.connect_s3()
    bucket = conn.lookup(bucket_name)
    return [k.name for k in bucket.list()]
    
def store_private_data(bucket_name, key_name, path_to_file):
    conn = boto.connect_s3()
    bucket = conn.lookup(bucket_name)
    key = bucket.new_key(key_name)
    #key = Key(bucket)
    #key.name = key_name
    
    data = 'this is a test string'
    key.set_contents_from_string(data)
    
    storedkey = bucket.lookup(key_name)
    storedvalue = storedkey.get_contents_as_string()
    assert data == storedvalue
    
    key.set_contents_from_filename(path_to_file)
    return key
    
def store_metadata_with_key(bucket_name, key_name, 
                            path_to_file, metadata):
    """
    Write the contents of a local file to S3 and also store custom metadata with the object.
    bucket_name key_name path_to_file metadata
    The name of the S3 Bucket.
    The name of the object containing the data in S3. Fully qualified path to local file.
    A Python dict object containing key/value
    data you would like associated with the object. 
    For example: {'key1':'value1', 'key2':'value2'}
    """
    s3 = boto.connect_s3()
    bucket = s3.lookup(bucket_name)
    # Get a new, blank Key object from the bucket. This Key object only 
    # exists locally until we actually store data in it.
    key = bucket.new_key(key_name)
    # Add the metadata to the Key object 
    key.metadata.update(metadata)
    #key.set_metadata() is anothor method
    # Now, write the data and metadata to S3 
    key.set_contents_from_filename(path_to_file)
    return key
    
def print_key_metadata(bucket_name, key_name): 
    """
    Print the metadata associated with an S3 Key object.
    bucket_name The name of the S3 Bucket.
    key_name The name of the object containing the data in S3. """
    s3 = boto.connect_s3()
    bucket = s3.lookup(bucket_name)
    key = bucket.lookup(key_name) 
    print key.metadata
    
def get_file(bucket_name, key_name):
    s3 = boto.connect_s3()
    bucket = s3.lookup(bucket_name)
    key = bucket.lookup(key_name)
    key.get_contents_to_filename('/Users/shenshen/Desktop/avatar.gif')
    return True

if __name__ == '__main__':
    #createbucket('jyblogtestbucket')
    print listkeys()
    #print store_private_data(bucket_name, 'test/Icon-50.png', '/Users/shenshen/Desktop/Icon-50.png')
    #print store_private_data(bucket_name, 'Icon-72', '/Users/shenshen/Desktop/Icon-72.png')
    #store_metadata_with_key(bucket_name, 'test/avatar', '/Users/shenshen/Desktop/avatar.gif', 
    #                        {'time':datetime.datetime.now(), 'desc':'a strange human'})
    #print_key_metadata(bucket_name, 'test/avatar')
    get_file(bucket_name, 'test/avatar')
