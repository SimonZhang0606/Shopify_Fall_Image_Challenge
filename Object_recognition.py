def localize_objects(input):

    #encoding to convert image file into base 64 string
    import base64

    def encode_image(image):
        with open(image, "rb") as image_file:
            return base64.b64encode(image_file.read())

    
    from google.oauth2 import service_account
    import os 

    #setup authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-key.json"
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/cloud-vision']
    SERVICE_ACCOUNT_FILE = 'service-key.json'
    
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """

    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(input, 'rb') as image_file:
        content = image_file.read()

    #transform image into 64_encoding
    image = encode_image(input)
    image = vision.Image(content=content)

    #calling google API to get the objects
    objects = client.object_localization(
        image=image).localized_object_annotations

    #compile result
    result = ""

    result += 'Number of objects found: {}'.format(len(objects))
    for object_ in objects:
        result += '\n{} (confidence: {})'.format(object_.name, object_.score)
        result += 'Normalized bounding polygon vertices: '
        for vertex in object_.bounding_poly.normalized_vertices:
            result += ' - ({}, {})'.format(vertex.x, vertex.y)
    
    result += "\n\n\n"

    file = open("output.txt", 'a')

    file.write(result)
    
    file.close()

localize_objects("./test_input/test_1.jpeg")

localize_objects("./test_input/test_2.jpeg")

localize_objects("./test_input/test_3.jpeg")

localize_objects("./test_input/test_4.jpeg")

localize_objects("./test_input/test_5.jpeg")

localize_objects("./test_input/test_6.jpeg")
