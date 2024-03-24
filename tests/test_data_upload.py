"""
Test valid and invalid CRUD operations on ImageUpload resource.
"""


import requests


user_url = 'http://localhost:5000/user'
image_url = 'http://localhost:5000/image'
files = {'file':open(r'C:\Users\Jilin\Desktop\DIYML\test_image.png','rb')}


def test_create_upload():
    # first create a test user testName
    params = {'user_name':'testName',
              'user_pass':'testPass'}
    response = requests.post(url=user_url,
                             params=params)
    assert response.status_code == 201 # created

    # then test the image uploading with the testName user
    params = {'user_name':'testName',
              'category':'apple'}
    response = requests.post(image_url,
                             params=params,
                             files=files)
    assert response.status_code == 201 # created


def test_delete_upload():
    # delete the test image file
    params = {'user_name':'testName',
              'image_name':'test_image.png'}
    response = requests.delete(url=image_url,
                               params=params)
    assert response.status_code == 202 # accepted

    # also cleanup the test user created
    params = {'user_name':'testName'}
    response = requests.delete(user_url,
                               params=params)
    assert response.status_code == 202 # accepted
