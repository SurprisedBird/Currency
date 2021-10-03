
URL = '/currency/contactus/create/'


def test_get_contactus(client):
    response = client.get(URL)
    assert response.status_code == 200


def test_post_empty_form(client):
    response = client.post(URL, data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }
    # assert ContactUs.objects.count() == contactus_initial_count


def test_invalid_form(client):
    form_data = {
        'email_to': 'test_invalid_form',
        'subject': 'test_subject'*100,
        'body': 'test_invalid_form',
    }

    response = client.post(URL, data=form_data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Enter a valid email address.'],
        'subject': ['Ensure this value has at most 255 characters (it has 1200).'], }


def test_valid_form(client):
    form_data = {
        'email_to': 'test_valid_form@ex.com',
        'subject': 'test_subject',
        'body': 'test_valid_form',
    }

    response = client.post(URL, data=form_data)
    assert response.status_code == 302
