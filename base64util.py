import base64
import pyperclip
import os


def image_to_base64(image_path, encoding):
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode(encoding)
    return base64_image


def base64_to_image(base64_path):
    with open(base64_path, "rb") as base64_file:
        image = base64.b64decode(base64_file.read())
    return image


def save_base64_to_file(base64_string, output_file):
    with open(output_file, "w") as file:
        file.write(base64_string)


def save_image_to_file(image_bytes, output_file):
    with open(output_file, "wb") as file:
        file.write(image_bytes)


def save_base64_to_clipboard(base64_image):
    pyperclip.copy(base64_image)


def validate_file_extension(file_path, extensions):
    _, extension = os.path.splitext(file_path)
    if extension in extensions:
        return True
    else:
        return False


def validate_file_path(file_path, extensions):
    if os.path.isfile(file_path):
        return validate_file_extension(file_path, extensions)
    else:
        return False
