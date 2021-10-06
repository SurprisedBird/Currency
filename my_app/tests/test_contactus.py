from currency.models import ContactUs

URL = '/currency/contactus/create/'


def test_get_contactus(client):
    response = client.get(URL)
    assert response.status_code == 200


def test_post_empty_form(client):
    contactus_initial_count = ContactUs.objects.count()
    response = client.post(URL, data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }
    assert ContactUs.objects.count() == contactus_initial_count


def test_invalid_form(client):
    contactus_initial_count = ContactUs.objects.count()
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
    assert ContactUs.objects.count() == contactus_initial_count


def test_valid_form(client):
    contactus_initial_count = ContactUs.objects.count()
    form_data = {
        'email_to': 'test_valid_form@ex.com',
        'subject': 'test_subject',
        'body': 'test_valid_form',
    }

    response = client.post(URL, data=form_data)
    assert response.status_code == 302
    assert response.url == "/index/"
    assert ContactUs.objects.count() == contactus_initial_count + 1
    contact_us_object = ContactUs.objects.last()
    assert contact_us_object.email_to == form_data['email_to']
    assert contact_us_object.subject == form_data['subject']
    assert contact_us_object.body == form_data['body']
