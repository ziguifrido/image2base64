import base64util as b64u
import argparse

BANNER = "\nImage2Base64\n"
ENCODING = "utf-8"
EXTENSIONS_BASE64 = ['.txt']
EXTENSIONS_IMAGE = ['.png', '.jpg', '.jpeg']


def save_to_clipboard(base64_image):
    b64u.save_base64_to_clipboard(base64_image)
    print("\n\nThe base64 has been copied to your clipboard!\n")


def save_to_file(base64_image, output_file_path):
    if not b64u.validate_file_extension(output_file_path, EXTENSIONS_BASE64):
        print(f"ERROR: Invalid output path: {output_file_path}")
    else:
        b64u.save_base64_to_file(base64_image, output_file_path)
        print(f"\n\nThe Base64 was saved to '{output_file_path}'.")


def main():
    parser = argparse.ArgumentParser(description='Convert Image to Base64')
    parser.add_argument("--input", type=str, help="Image Path (input)")
    parser.add_argument("--output", type=str, help="Base64 Path (output)")
    parser.add_argument("--output_type", type=str, help="Output Type: 1- Clipboard (default); 2- File;")
    args = parser.parse_args()

    print(BANNER)

    try:
        if not args.input:
            image_path = input("Please enter the path of the image you want to convert to base64: ")
        else:
            image_path = args.input

        if not b64u.validate_file_path(image_path, EXTENSIONS_IMAGE):
            print(f"ERROR: Invalid Image path: {image_path}")
        else:
            base64_image = b64u.image_to_base64(image_path, ENCODING)

            if not args.output_type:
                option = input("\n\nOptions:\n 1: Save to clipboard (default); \n 2: Save to file;\n\n:")
            else:
                option = args.output_type

            if option.strip() != "2":
                save_to_clipboard(base64_image)
            else:
                if not args.output:
                    output_file_path = input("Enter the output file path to save the Base64: ")
                else:
                    output_file_path = args.output
                
                save_to_file(base64_image, output_file_path)
                
    except FileNotFoundError:
        print("ERROR: Invalid Path!")


if __name__ == "__main__":
    main()
